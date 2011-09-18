=================
Webとデータベース
=================

PHP
===

Apache/mod_phpで動かすことがほとんど。

.. code-block:: php

   <?php
   echo "Hello world!\n";

CUI版のPHPもある。

::

   $ sudo aptitude install php5-cli

::

   $ php hello.php

ApacheとPHPの関係とか
---------------------

ApacheがHTTPサーバの機能を提供し、Apacheモジュールであるmod_phpがphpのスクリプトファイルを実行する。

URLルーティング
===============

CGIなどのサーバ側で実行されるスクリプトは、URLと実行するスクリプトのファイルパスが一対一の密結合になっていた。

この場合、動的なURLを扱うのが難しく、スクリプトファイルの構造化もやりづらかった。

こういった場合に、URLルーティングの仕組みを導入して解決することができる。

基本的には1つのスクリプトファイルがすべてのリクエストを受け取り、そこから処理を他のスクリプトに委譲したりする。

Apacheであればmod_rewriteを使ってindex.phpを隠蔽するなどがよくあるやり方。

WSGI
====

WebサーバとPythonのWebアプリケーションをつなぐ、共通のインターフェース。

memcached
=========

物理メモリを使用するシンプルなキャッシュサーバ。

クライアントライブラリはいっぱいある。

::

   $ sudo aptitude install memcached


起動はこんな感じ。デフォルトだと11211ポートを使う。

::

   $ memcached -p 11211 -m 32 -l 127.0.0.1

認証はないので、外部から接続可能なサーバで使う場合は注意する。

MySQL
=====

SQLで問い合わせ可能なデータベース。

認証と権限の設定が可能。

最新の安定版は5.5。

古いバージョンは文字コード周りのトラブルや性能差がかなりあるので、可能なら最新版を使うべき。

ODBC/JDBC
=========

データベース接続の共通インターフェース。

ODBCはWindows標準。

JDBCはJava用。

ADO->OLEDB->ODBC->各種データベースという関係。

ADOは **ActiveX Data Object** の略。OLEDBのデータをオブジェクトとして扱えるようにするインターフェース。

VBScript
========

WindowsScriptHostで実行できるスクリプト。CreateObject関数でOLEコンテナ(Excelとか)とかActiveXのオブジェクトを扱えるので、
VBScriptに機能がなくても外部アプリケーションとの連携でいろいろできる。

前述のADOをCreateObject関数で作れば、ODBC経由のデータベースサーバを扱うことも可能。

IIS
===

MicrosoftのHTTPサーバ。ISAPIというインターフェース経由で各種モジュールを組み込むことが可能。

ISAPI経由でphpを動かすこともできる。

またWSHのスクリプトを実行して出力を返す **Active Server Pages** も使える。

Windows ServerやWindowsXP Proなどで使える。
