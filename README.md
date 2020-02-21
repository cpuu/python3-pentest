# 모의 침투 입문자를 위한 파이썬 3 활용
## [ 파이썬 3 기반의 TCP/IP 활용 지침서]

![image](./python3-pentest.jpg)

이 저장소에는 [모의 침투 입문자를 위한 파이썬 3 활용 - 파이썬 3 기반의 TCP/IP 활용 지침서](http://acornpub.co.kr/book/python3-pentest) 도서의 예제 소스코드를 포함하고 있습니다.

## 이 책에 관하여
데비안/우분투 계열의 운영 체제에서 제공하는 파이썬 3.4를 이용해 TCP/IP 소켓을 구현하고, 이를 기반으로 주요한 모의 침투 도구의 구현 과정을 소개한다. 모든 내용을 파이썬 3에 기반해 작성하였으며, 소스 코드에 비중을 두고 최대한 이해하기 쉽게 주석을 달고 순차적인 구현 과정을 제시한다. 또한 Github를 통해 본문에서 사용한 소스 코드를 지속적으로 제공한다.

## 소스코드 구성
각 소스코드는 책의 각 장별로 폴더로 구분되어 있습니다. 소스코드는 아래와 같이 파이썬 언어의 문법 규약을 따릅니다.

```
def dequeue(self):
    if not self.outbound_stack:
        while self.inbound_stack:
            self.outbound_stack.append(self.inbound_stack.pop())
    return self.outbound_stack.pop()
```

해당 소스코드는 파이썬 3.4 버전을 대상으로 합니다.

## 함께 읽으면 좋은 도서
* [해킹 입문자를 위한 TCP/IP 이론과 보안 2/e - 모의 침투 입문자를 위한 필독서](http://acornpub.co.kr/book/hacking-tcpip2)

* [해커의 언어 파이썬 3 입문](http://acornpub.co.kr/book/python3-for-hacker)

## 문의
도서를 구입해주셔서 감사합니다. 문의사항이 있으시거나 내용 중 도서 오류 또는 오탈자 제보가 필요하신 경우 cpuu@icloud.com 또는 [출판사 홈페이지](http://acornpub.co.kr/contact/errata)를 통해 알려주시기 부탁드립니다.
