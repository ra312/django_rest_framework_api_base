curl http://localhost:8000/api/v1/1/
echo "\n adding new employee ..."
curl -X POST http://localhost:8000/api/v1/ -d "title=frontend_engiiner&name=unique&department=ever_after_fun&description=hi there"
curl http://localhost:8000/api/v1/1/
