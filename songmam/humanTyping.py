import random
import asyncio
from time import sleep
from typing import Awaitable

class HumanTyping:
    # https://humanbenchmark.com/tests/typing
    word_per_min = 80

    @property
    def charactor_per_min(self):
        # English Estimate
        return self.word_per_min * 5

    @property
    def gap_between_seen_and_start_typing(self):
        """
        in milisecond
        """
        return random.normalvariate(100,100)

    async def act_typing(self, text, typing_func: Awaitable, stop_typing_func: Awaitable):
        duration_min = len(text) / self.charactor_per_min
        num_of_word = len(text) / 5
        num_of_sentence = num_of_word // 5
        duration_sec = duration_min * 60
        num_of_pause = min(round(random.paretovariate(2)), max(num_of_sentence, 3))
        remain_pause = num_of_pause
        remain_time = duration_sec
        while True:
            await asyncio.sleep(0.3)
            await typing_func()
            if remain_pause == 0:
                await asyncio.sleep(remain_time)
                await stop_typing_func()
                break
            else:
                type_for = random.random() * remain_time
                remain_time -= type_for
                await asyncio.sleep(type_for)
                remain_pause -= 1 
            await stop_typing_func()
    
    # async def act_typing_simple(self, text, typing_func: Awaitable, stop_typing_func: Awaitable):
    #     duration_min = len(text) /  self.charactor_per_min
    #     num_of_word = len(text) / 5
    #     num_of_sentence = num_of_word // 5
    #     duration_sec = duration_min * 60
    #     num_of_pause = min(round(random.paretovariate(2)), max(num_of_sentence, 3))
    #     remain_pause = 0
    #     remain_time = duration_sec
    #     while True:
    #         await asyncio.sleep(0.3)
    #         await typing_func()
    #         if remain_pause == 0:
    #             await asyncio.sleep(remain_time)
    #             await stop_typing_func()
    #             break
    #         else:
    #             type_for = random.random() * remain_time
    #             remain_time -= type_for
    #             await asyncio.sleep(type_for)
    #             remain_pause -= 1
    #         await stop_typing_func()

    def act_typing_simple(self, text, typing_func: callable, stop_typing_func: callable):
        duration_min = len(text) / self.charactor_per_min
        duration_sec = duration_min * 60
        typing_func()
        sleep(duration_sec)
        stop_typing_func()

def type_sth():
    print('im typing.')

if __name__ == '__main__':
    from functools import partial
    ht = HumanTyping()
    print('receiving msg')
    stop_typing = partial(print, "im done.", end=' ')
    ht.act_typing_simple("aiusdhjashfdjo;ahodfhoawsfi", type_sth, stop_typing)
    print('sending msg')