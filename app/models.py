from enum import Enum

from pydantic import BaseModel, Field


class OpenCCConfig(str, Enum):
    s2t = "s2t.json"
    t2s = "t2s.json"
    s2tw = "s2tw.json"
    tw2s = "tw2s.json"
    s2hk = "s2hk.json"
    hk2s = "hk2s.json"
    s2twp = "s2twp.json"
    tw2sp = "tw2sp.json"
    t2tw = "t2tw.json"
    hk2t = "hk2t.json"
    t2hk = "t2hk.json"
    t2jp = "t2jp.json"
    jp2t = "jp2t.json"
    tw2t = "tw2t.json"


CONFIG_DESC = """
s2t.json Simplified Chinese to Traditional Chinese 簡體到繁體
t2s.json Traditional Chinese to Simplified Chinese 繁體到簡體
s2tw.json Simplified Chinese to Traditional Chinese (Taiwan Standard) 簡體到臺灣正體
tw2s.json Traditional Chinese (Taiwan Standard) to Simplified Chinese 臺灣正體到簡體
s2hk.json Simplified Chinese to Traditional Chinese (Hong Kong variant) 簡體到香港繁體
hk2s.json Traditional Chinese (Hong Kong variant) to Simplified Chinese 香港繁體到簡體
s2twp.json Simplified Chinese to Traditional Chinese (Taiwan Standard) with Taiwanese idiom 簡體到繁體（臺灣正體標準）並轉換爲臺灣常用詞彙
tw2sp.json Traditional Chinese (Taiwan Standard) to Simplified Chinese with Mainland Chinese idiom 繁體（臺灣正體標準）到簡體並轉換爲中國大陸常用詞彙
t2tw.json Traditional Chinese (OpenCC Standard) to Taiwan Standard 繁體（OpenCC 標準）到臺灣正體
hk2t.json Traditional Chinese (Hong Kong variant) to Traditional Chinese 香港繁體到繁體（OpenCC 標準）
t2hk.json Traditional Chinese (OpenCC Standard) to Hong Kong variant 繁體（OpenCC 標準）到香港繁體
t2jp.json Traditional Chinese Characters (Kyūjitai) to New Japanese Kanji (Shinjitai) 繁體（OpenCC 標準，舊字體）到日文新字體
jp2t.json New Japanese Kanji (Shinjitai) to Traditional Chinese Characters (Kyūjitai) 日文新字體到繁體（OpenCC 標準，舊字體）
tw2t.json Traditional Chinese (Taiwan standard) to Traditional Chinese 臺灣正
"""


class OpenCCReq(BaseModel):
    text: str = Field(description="text to be converted")
    config: OpenCCConfig = Field(description=CONFIG_DESC)


class OpenCCResp(BaseModel):
    text: str = Field(description="converted text")
