# コメダ珈琲おまかせガチャ
### Video Demo:  https://youtu.be/JOiGcSinTeY
### URL: https://komeda-gacha.herokuapp.com

#### Description:
  サイゼリヤ1000円ガチャにインスパイヤを受けてコメダ珈琲おまかせガチャを作りました。
  
  1000円ガチャの機能に加えて、1500円、2000円、主食ドリンクデザートから1品ずつ選択するバランスモードを作りました。
  
  もともとメニューのデータはSQLiteに搭載していたのですが、HerokuにホストするときにSQLiteではうまく動かなかったのでCSVを直接読み取る方式に変更してあります。
  
  メニューのデータが増えてきたり、アクセス数が増加してきたときにボトルネックになりそうだと思っています。
  
  今回WEBサイトを作るのはほぼ初めてだったので、HTMLやCSSの知識をたくさんインプットし、アウトプットしました。特にMeta name descriptionやfavicon.icoなどいままで知らなった機能を実装しました。
  
#### Usage:
  それぞれのページをクリックして移動。トップページに戻るにはタイトルをクリックする。
  ツイートボタンを押して結果をそのままツイートできる。
  
#### Troubles:
  一番苦労したのがHerokuへのデプロイだった。HerokuでWebサイトをホストするのは初めてで、Procfileの設定にとても苦労した。
  
  最初Procfileとすべきところをprocfileでコミットしてしまい、ファイル名をリネームしてコミットしたが認識されず、Procfileを削除してから削除をコミットして、 Procfileをコミットしなおした。
  
  ここで解決するのにたくさんの時間を要した。
  
#### Growth:
 gitの仕様上ファイル名のリネームは差異として認識されないことを知った。
  
#### Technologies:
  - Python
  - Flask
  - HTML
  - CSS
  - (SQLite)

#### Infrastructure:
  Heroku Free Plan
  

#### Description:
  Inspired by the Saizeriya 1000 Yen Gacha, I made Komeda Coffee Omakase Gacha.
  
  In addition to the function of 1000 yen gacha, we have created a balance mode where you can select one item at a time from 1500 yen, 2000 yen, and staple drinks and desserts.
  
  Originally, the menu data was installed in SQLite, but when hosting it on Heroku, it did not work well in SQLite, so I changed it to a method that reads CSV directly.
  
  I think it will become a bottleneck when the menu data increases and the number of accesses increases.
  
  It was almost the first time to create a website this time, so I input and output a lot of knowledge about HTML and CSS. In particular, we have implemented features that we have   known so far, such as Meta name description and favicon.ico.
  
#### Usage:
  Click each page to move. Click the title to return to the top page.
  You can tweet the result as it is by pressing the tweet button.
  
#### Troubles:
  The hardest part was deploying to Heroku. It was my first time hosting a website on Heroku and I had a lot of trouble setting up my Procfile.
  
  I first committed what should be a Procfile with a procfile, renamed the file and committed, but it was not recognized, I deleted the Procfile and then committed the deletion
  
#### Growth:
  Recommitted the Procfile. I learned that renaming file names is not recognized as a difference due to the specifications of git.
  
#### Technologies:
  - Python
  - Flask
  - HTML
  - CSS
  - (SQLite)

#### Infrastructure:
  Heroku Free Plan
