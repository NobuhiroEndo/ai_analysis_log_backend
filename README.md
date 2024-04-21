# ai_analysis_log_backend
### ■ 概要
- 課題のバックエンド。フロント(React)側から送られてきたPOSTリクエストを整形処理し、データベースに保存する。
- 登録されたレコードは、管理画面の『Ai_analysis_logs』から閲覧可能。
### ■ URL
1. POSTエンドポイント：https://ai-analysis-log.nein-februar.com/ai_analysis_logs/create/
2. 管理画面：https://ai-analysis-log.nein-februar.com/admin/
3. モックAPI：https://7qpvy8fkel.execute-api.ap-northeast-1.amazonaws.com/dev/ai_analysis_log
### ■ バックエンド・インフラ使用技術
1. Django rest framework(3.15.1)
2. Django (5.0.4)
3. Python (3.12.3)
4. VPC
5. EC2(nginx, gunicorn)
6. ALB
7. Certificate Manager
8. Route53
10. Lambda(モックAPIに使用)
11. Api Gateway(モックAPIに使用)
