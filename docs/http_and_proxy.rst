==================
HTTPとプロキシの話
==================

HTTPのおさらい
==============

どんなプロトコルか
------------------

**ブラウザからのリクエスト**::

   GET / HTTP/1.1
   Host: 127.0.0.1:8000
   Connection: keep-alive
   Cache-Control: max-age=0
   User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
   Accept-Encoding: gzip,deflate,sdch
   Accept-Language: ja,en-US;q=0.8,en;q=0.6
   Accept-Charset: Shift_JIS,utf-8;q=0.7,*;q=0.3

**サーバから返すレスポンス**::

   HTTP/1.0 200 OK
   Content-Type: text/plain
   Content-Length: 12
   
   Hello world!

**サーバ例**:

.. code-block:: python

   import socket
   
   content = 'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\n\r\nHello world!'
   
   ADDR = '127.0.0.1'
   PORT = 8000
   
   def main():
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
       print 'Starting HTTP server port=%s' % PORT
       s.bind((ADDR, PORT))
       s.listen(1)
       try:
           while True:
               conn, addr = s.accept()
               print '---connected---'
               try:
                   data = conn.recv(1024)
                   print data
                   print '-------------------------'
                   conn.send(content)
               finally:
                   conn.close()
       except KeyboardInterrupt:
           pass
   
   if __name__ == '__main__':
       main()


ステートレス
------------

プロトコル自体の仕様では、サーバ側で状態を持たないもの。

ステートフルなプロトコルは例えばFTPやSMTP。

ステートフルどうすんの
----------------------

でもログインの実装とかは状態保持が必要。そういう場合にはHTTP Cookieを利用できる。

サーバ側からCookieを設定したい場合には、Set-Cookieヘッダを返す。

Cookieはクライアント側で変更可能なため、信頼できない値となる。

プロキシサーバ
==============

通信を中継するサーバ。

HTTPとプロキシ
==============

HTTPでの接続先はリクエストヘッダ中のHostヘッダで決まる。

そのため、リクエスト内容を解析しなければ、接続先がわからない。

プロキシサーバのソフトウェアとしては、Apacheでmod_proxyモジュールとmod_proxy_httpモジュールの組み合わせなどがある。

sshとプロキシ
=============

ポートフォワード
----------------

::

   $ ssh -L 5000:127.0.0.1:8000 foo@example.com

SOCKS
-----

パケット転送先も指定可能なプロトコル。VPNに少し似ている(片方向のみ)。

SOCKSサーバにSOCKSクライアントで接続して利用できる。ブラウザのプロキシサーバ設定にもある。

::

   $ ssh -D 6000 foo@example.com

実装
====

サーバ用のソケットをlistenして待つ。クライアント側から接続があれば、転送先に向けてクライアント用のソケットでconnectする。

改ざんについて
==============

プロキシサーバで、通信データを転送する際に、中身を変更することができる。

これを利用してリクエストやレスポンスの改ざんを行なう。

クライアント端末の接続先をプロキシサーバに向けさせても、ユーザはなかなか気付きにくい。

認証情報の入力を求める表示をレスポンスに含ませ、データを抜き取ることも可能となる。

SSLを使うと、通信内容が暗号化されて中継サーバでは解析が難しいため、こういった改ざんも難しくなる。
