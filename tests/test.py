# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from textrankr import TextRank


class TestReordered(unittest.TestCase):

    def setUp(self):
        self.text = "'지능정보기술연구소' 연말 출범 (서울=연합뉴스) 고상민 기자 = 민간 주도의 인공지능(AI) 연구단체 '지능정보기술연구소'가 이르면 올해 안에 출범할 것으로 보인다. 연구소 설립을 주도하는 소프트웨어정책연구소(SPRi)는 3일 서울 중구 프레스센터에서 기자간담회를 열고 \"인공지능 기술을 본격적으로 연구할 단체를 이르면 연내 발족할 계획\"이라면서 \"다음 달까지 법인을 설립해 인력채용에 나설 예정\"이라고 밝혔다. 이 연구소는 미래창조과학부가 지난 3월 대통령 주재 민관합동 간담회에서 발표한 '지능정보산업 발전전략'의 한 축이다. 이미 SK텔레콤, KT, 삼성전자, LG전자, 현대자동차, 네이버, 한화생명 등 7개 업체가 30억 원씩 출자했으며 주식회사 형태로 설립된다. 미래부는 SPRi, 정보통신기술진흥센터(KISDI)와 함께 후방에서 지원한다. 연구소 설립추진 단장을 맡은 김진형 SPRi 소장은 이날 간담회에서 \"연구소가 설립되면 향후 5년간 1년에 300억 원 정도를 정부에서 지원받아 인공지능 기술 연구에 쓸 수 있다\"면서 \"연구원 규모는 50명 안팎으로 꾸릴 예정\"이라고 말했다. 김 소장은 정부가 연구소 설립을 결정한 데에는 국내 인공지능 연구를 경쟁체제로 만들려는 의도가 다분하다고 설명했다. 이는 기존에 AI 연구도 병행해 온 한국전자통신연구원(ETRI·에트리)을 염두에 둔 발언이었다. 그는 \"인공지능을 비롯해 소프트웨어 분야는 똑같은 기술을 연구할 필요가 없다\"면서 \"에트리가 이미 진행한 연구가 있다면 해당 부분은 (돈을 주고) 사다 쓰면 될 일\"이라고 말했다. 김 소장이 현재 가장 주력하는 건 '인재 모집'이다. AI 전문가뿐만 아니라 이들을 뒷받침할 컴퓨팅 전문가들도 절실히 필요한 만큼 내로라하는 글로벌 IT 기업이나 대학을 찾아가 삼고초려를 해서라도 우수 인력을 데려올 계획이다. 김 소장은 \"연구소란 우수 인재들의 성장 발판이 돼야 하는데 우리나라 기존 연구소들은 그런 역할을 하지 못했던 게 사실\"이라며 \"이번 연구소는 인공지능 인재들이 한 번쯤 거쳐야 하는 필수 코스가 되도록 자리매김해야 한다\"고 강조했다. 그는 \"연구소 위치는 아직 확정되지 않았다\"면서 \"연말 개소식에 앞서 AI와 관련한 세계적인 석학들을 초청해 국제학술콘퍼런스를 열 계획\"이라고 말했다."

    def test_ranked(self):
        textrank = TextRank(self.text)
        self.assertEqual(textrank.reordered[0].text, "연구소 설립을 주도하는 소프트웨어정책연구소(SPRi)는 3일 서울 중구 프레스센터에서 기자간담회를 열고 \"인공지능 기술을 본격적으로 연구할 단체를 이르면 연내 발족할 계획\"이라면서 \"다음 달까지 법인을 설립해 인력채용에 나설 예정\"이라고 밝혔다.")


if __name__ == '__main__':
    unittest.main()
