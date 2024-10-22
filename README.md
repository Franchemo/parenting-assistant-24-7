# AI Parenting Assistant (AI育儿助手)

An intelligent parenting assistant powered by OpenAI's GPT models and Streamlit, designed to provide personalized parenting advice and support.

## Features

- Personalized parenting advice based on:
  - Child's age and personality
  - Family situation
  - Language environment
  - Siblings information
  - Kindergarten status
  - Child's interests and hobbies
- Real-time chat interface
- Multiple question categories:
  - General parenting issues
  - Health concerns
  - Behavior management
- Detailed subcategories for specific parenting topics
- Chat history maintenance
- User-friendly interface

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Franchemo/parenting-assistant-24-7.git
cd parenting-assistant-24-7
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key and Assistant ID:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_ASSISTANT_ID=your_assistant_id_here
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Fill in the initial questionnaire about your child and family situation
2. Select the type of parenting question you have
3. Choose specific subcategories if applicable
4. Enter your question in the chat interface
5. Receive personalized advice based on your specific situation

## Technologies Used

- Python
- Streamlit
- OpenAI API
- Python-dotenv

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
