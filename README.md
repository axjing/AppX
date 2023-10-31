# idealX
人工智能应用平台

## 目录

[TOC]

## 安装环境
### python 后端安装
```sh
pip install -r requirements.txt
```
### react前端安装
1. 创建一个新的React应用：
```sh
npm create-react-app user-auth-app
cd user-auth-app
```
2. 安装axios库以便进行HTTP请求：
```sh
npm install axios
```

## 使用说明
1. 启动运行FastAPI应用程序
```sh
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
2. 然后，您可以在浏览器或API测试工具中访问 `http://127.0.0.1:8000/docs`，使用自动生成的交互式文档测试这两个端点。您还可以使用API请求库（如requests）来与这些端点进行交互。
3. 运行React应用：
```sh
cd frontend
npm start
```


## Reference

## 补充

### MySQL使用
