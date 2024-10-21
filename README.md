# AI育儿助手

这是一个使用Streamlit和OpenAI API构建的AI育儿助手应用。

## 安装

1. 克隆此仓库到本地机器。
2. 进入项目目录：
   ```
   cd ai_parenting_assistant
   ```
3. 安装所需的依赖：
   ```
   pip install -r requirements.txt
   ```

## 设置OpenAI API密钥

在运行应用之前，您需要设置OpenAI API密钥。请按照以下步骤操作：

1. 获取OpenAI API密钥：如果您还没有API密钥，请访问 [OpenAI](https://openai.com/) 网站并注册一个账户以获取API密钥。

2. 设置环境变量：
   - 在macOS或Linux上，在终端中运行：
     ```
     export OPENAI_API_KEY='your-api-key-here'
     ```
   - 在Windows上，在命令提示符中运行：
     ```
     set OPENAI_API_KEY=your-api-key-here
     ```

   请将'your-api-key-here'替换为您的实际API密钥。

## 运行应用

设置好API密钥后，您可以通过以下命令运行应用：

```
streamlit run app.py
```

应用将在您的默认web浏览器中打开，通常地址为 http://localhost:8501。

## 使用说明

1. 选择问题类型（育儿问题、健康问题或行为管理）。
2. 如果选择了"育儿问题"，还可以进一步选择具体的问题类型。
3. 在输入框中输入您的育儿问题。
4. 点击发送或按回车键提交问题。
5. AI助手将生成回答并显示在聊天窗口中。
6. 您可以继续提问，与AI助手进行对话。
7. 如果想开始新的对话，可以点击"清空对话"按钮。

希望这个AI育儿助手能为您提供有用的育儿建议和支持！
