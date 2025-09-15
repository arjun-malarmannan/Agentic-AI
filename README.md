# 🎨 CultPass Marketing Agent

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A sophisticated AI-powered application to help CultPass Marketing Analysts create compelling content for promoting cultural experiences to B2B clients using an intelligent marketing agent.

![CultPass Demo](https://img.shields.io/badge/Demo-Live-brightgreen.svg)

## 🏢 About CultPass

CultPass is a B2B company that developed a benefits card for companies to offer their employees access to cultural experiences including:

- 🏛️ **Museums & Art Galleries**
- 🎵 **Concerts & Live Performances** 
- 🎭 **Theater & Shows**
- 🎨 **Art Workshops & Classes**
- 🎪 **Cultural Festivals**
- 🏰 **Historical Tours**

## ✨ Features

- 🤖 **AI Content Generation**: Create marketing materials using OpenAI GPT-4o-mini
- 📊 **Campaign Planning**: Strategic content planning for B2B marketing campaigns
- 🎯 **Multi-Channel Support**: Email, social media, brochures, presentations, and more
- 🏭 **Industry Targeting**: Customized content for different business sectors
- 📱 **Responsive Web UI**: Modern, mobile-friendly interface
- 📈 **Content History**: Track and reuse generated content
- ⚙️ **Configurable Parameters**: Adjust tone, audience, and cultural focus

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API key (Vocareum endpoint supported)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arjun-malarmannan/Marketing-Agent.git
   cd Marketing-Agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

5. **Run the application**
   ```bash
   # Demo mode (no API key required)
   python app_demo.py
   
   # Production mode (requires API key)
   python app.py
   ```

6. **Open your browser**
   ```
   http://localhost:5000
   ```

## 🎯 Usage Examples

### Content Generation
Generate marketing content for different channels and audiences:
- Email campaigns for HR managers
- LinkedIn posts for tech companies
- Instagram content for startups
- Brochure copy for healthcare organizations

### Campaign Planning
Create comprehensive marketing strategies with:
- Timeline and milestones
- Budget allocation
- Success metrics
- Cultural event integration

## 🛠️ Project Structure

```
cultpass-marketing/
├── app.py                    # Main Flask application (production)
├── app_demo.py              # Demo version with simulated responses
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── templates/              # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Landing page
│   ├── content_generator.html  # Content creation interface
│   └── campaign_planner.html  # Campaign strategy interface
├── complete_exercise.py    # OpenAI SDK exercise implementation
├── working_exercise.py     # Working demo of all concepts
└── docs/                   # Additional documentation
    ├── EXERCISE_SUMMARY.md # Detailed exercise completion guide
    └── PROJECT_COMPLETE.md # Final project summary
```

## 🎓 Learning Objectives

This project demonstrates:

1. **OpenAI SDK Integration**: Complete API setup and usage
2. **Python Web Development**: Flask application with RESTful APIs
3. **AI Prompt Engineering**: Effective system and user prompts
4. **Business Application**: Real-world marketing use case
5. **Error Handling**: Comprehensive exception management
6. **UI/UX Design**: Modern, responsive web interface

## 🧪 Exercise Completion

This project successfully completes the OpenAI SDK exercise with:

- ✅ **Step 1**: Client instantiation with Vocareum endpoint
- ✅ **Step 2**: Model parameters (gpt-4o-mini, temperature=0.7)
- ✅ **Step 3**: Business-specific system prompt
- ✅ **Step 4**: Reusable content generation function
- ✅ **Step 5**: Proper function execution
- ✅ **Step 6**: Parameter experimentation and testing

### Key Fixes Applied:
- Fixed `temperature = [0.0, 20]` → `temperature = 0.7`
- Added missing user message in API calls
- Corrected function parameter passing
- Enhanced error handling

## 🚀 Deployment Options

### Local Development
```bash
python app_demo.py  # Demo mode
python app.py       # Production mode
```

### Docker (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Cloud Deployment
- **Heroku**: Ready for deployment with Procfile
- **Vercel**: Serverless deployment support
- **AWS/GCP**: Container or serverless options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for the powerful GPT-4o-mini API
- Flask community for the excellent web framework
- Bootstrap for the responsive UI components
- Vocareum for the educational OpenAI endpoint

## 📞 Support

For questions or support:
- 📧 Email: support@cultpass.com
- 💬 Issues: [GitHub Issues](https://github.com/arjun-malarmannan/Marketing-Agent/issues)
- 📖 Docs: [Project Wiki](https://github.com/arjun-malarmannan/Marketing-Agent/wiki)

## 🔗 Links

- [Live Demo](http://localhost:5000) (when running locally)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Bootstrap Documentation](https://getbootstrap.com)

---

**Built with ❤️ for marketing professionals who want to leverage AI for creative content generation.**
