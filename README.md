# AI Parenting Assistant | AI育儿助手

A bilingual (English/Chinese) AI parenting assistant powered by OpenAI's GPT models and Streamlit, designed to provide personalized parenting advice and support.

一个基于OpenAI GPT模型和Streamlit的双语（英文/中文）AI育儿助手，旨在提供个性化的育儿建议和支持。

## Features | 功能

- Bilingual support (English/Chinese) | 双语支持（英文/中文）
- Personalized parenting advice based on: | 基于以下信息的个性化育儿建议：
  - Child's age and personality | 孩子的年龄和性格
  - Family situation | 家庭情况
  - Language environment | 语言环境
  - Siblings information | 兄弟姐妹信息
  - Kindergarten status | 幼儿园状态
  - Child's interests and hobbies | 孩子的兴趣爱好
- Real-time chat interface | 实时聊天界面
- Multiple question categories: | 多种问题类别：
  - General parenting issues | 育儿问题
  - Health concerns | 健康问题
  - Behavior management | 行为管理
- Detailed subcategories for specific parenting topics | 具体育儿主题的详细子类别
- Chat history maintenance | 聊天历史记录维护
- User-friendly interface | 用户友好的界面

## Setup | 设置

1. Clone the repository | 克隆仓库:
```bash
git clone https://github.com/Franchemo/parenting-assistant-24-7.git
cd parenting-assistant-24-7
```

2. Install dependencies | 安装依赖:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key and Assistant ID | 在根目录创建`.env`文件并添加您的OpenAI API密钥和Assistant ID:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_ASSISTANT_ID=your_assistant_id_here
```

4. Run the application | 运行应用:
```bash
streamlit run app.py
```

## Usage | 使用方法

1. Select your preferred language (English/Chinese) from the sidebar | 从侧边栏选择您偏好的语言（英文/中文）
2. Fill in the initial questionnaire about your child and family situation | 填写关于您的孩子和家庭情况的初始问卷
3. Select the type of parenting question you have | 选择您的育儿问题类型
4. Choose specific subcategories if applicable | 选择具体的问题子类别（如适用）
5. Enter your question in the chat interface | 在聊天界面输入您的问题
6. Receive personalized advice based on your specific situation | 获取基于您具体情况的个性化建议

## Technologies Used | 使用的技术

- Python
- Streamlit
- OpenAI API
- Python-dotenv

## Contributing | 贡献

Feel free to submit issues and enhancement requests! | 欢迎提交问题和改进建议！

## License | 许可证

This project is licensed under the MIT License - see the LICENSE file for details. | 本项目采用MIT许可证 - 详见LICENSE文件。

## Support | 支持

If you encounter any issues or need assistance, please create an issue in the repository. | 如果您遇到任何问题或需要帮助，请在仓库中创建issue。

## Deployment | 部署

The application can be deployed on Streamlit Cloud or any other Python-compatible hosting service. | 应用程序可以部署在Streamlit Cloud或任何其他支持Python的托管服务上。

To deploy on Streamlit Cloud: | 在Streamlit Cloud上部署：
1. Fork this repository | 复制此仓库
2. Sign up for Streamlit Cloud | 注册Streamlit Cloud
3. Create a new app pointing to your forked repository | 创建指向您的仓库的新应用
4. Add your environment variables in the Streamlit Cloud dashboard | 在Streamlit Cloud仪表板中添加您的环境变量
