from typing import List

from temperatures import AverageTemperatures


class TiempoPipeline:
    _result: List[AverageTemperatures] = []

    def process_item(self, item: AverageTemperatures, spider):
        self._result.append(item)
        return item

    @classmethod
    def get_result(cls) -> AverageTemperatures:
        ret = None
        if cls._result:
            ret = cls._result[0]
            cls._result = []
        return ret
