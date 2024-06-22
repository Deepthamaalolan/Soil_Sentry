# **The Problem**
Farming accounts for 85% of total global water use, and alarmingly, 40% of this water is wasted. Farmers often overwater certain parts of their crops, resulting in a significant amount of waste water that could be better utilized to nourish dried-out areas or support our growing population, especially in an era where climate change is making water resources increasingly scarce. The need for optimized water allocation in agriculture is critical.

# **Our Solution**
Soil Sentry is a mobile app that combines accessible sensor technology with AI to monitor soil moisture levels and offer AI-driven insights and recommendations to farmers. This solution ensures efficient and sustainable water management practices, reduces water wastage, and improves crop yields.

![image](https://github.com/Deepthamaalolan/Soil_Sentry/assets/46663016/c0a7c53b-cbd6-4b57-8a86-664706e036cd)

# **Key Features**
  1. Real-Time Soil Moisture Monitoring: Integrates with soil moisture sensors to provide accurate, real-time data on soil conditions. Farmers receive alerts and notifications when soil moisture levels fall below or exceed optimal thresholds, ensuring timely intervention.
  2. Drone Integration: Connects with drones to gather aerial data on crop health and soil conditions, predicting issues like soil salinity and advising farmers on preventive measures.
  3. AI Chatbot: Farmers can ask customized questions about their irrigation practices, crop management, and more. The chatbot also incorporates weather forecasts to predict water needs and adjust irrigation schedules.
  4. Crop Recommendations: Suggest crops based on the season and changes in soil conditions throughout the year.
  5. Water Demand Forecasting: Analyzes historical data, weather patterns, and crop requirements to ensure efficient distribution of water resources.
  6. Smart Irrigation Systems: Automates control based on real-time soil moisture data and AI recommendations, integrating with existing systems to save both time and water.
  7. Leak Detection: Detects potential leaks in irrigation systems, reducing water loss by sending alerts and maintenance recommendations.
  8. Water Tank Monitoring: Tracks the usage of water tanks and rain tanks separately, providing real-time data on water levels, detecting leaks, and sending alerts.

# **Technological Architecture**

![image](https://github.com/Deepthamaalolan/Soil_Sentry/assets/46663016/f55d033c-4850-429e-8adf-54d6d50bd1d2)

- Frontend: React Native, React
- Backend: Node.js, Python
- AI: GPT-3.5 for chatbot, Salesforce Einstein for prediction models
- Database: MongoDB
- Data Visualization: Tableau
- API: National Weather Service API
- Data Structuring: Unstructured.io
- Cloud Infrastructure: Salesforce
- In-house RAG System: Leverages vector search capabilities to train our LLM model

# **Setup Instructions**
(Instructions on how to run the project)
  1. Start by running the backend server. Open a terminal, navigate to the Backend directory, and run python weather.py.
  2. In another terminal, go to the Client directory and execute npm start. This will launch a chatbot for you to interact with.
  3. Do add your OpenAI API key into the .env file 

# **Contributing**
  We welcome contributions to this project! If you have experience in AI, sensor technology, or agriculture, feel free to:

- Fork the repository and create a pull request with your contributions.
- Raise issues to report bugs or suggest improvements.

# **License**
  Released under MIT.

**Disclaimer**
Soil Sentry is intended to help farmers optimize water usage and irrigation practices. It should not be used as a replacement for professional agricultural advice.




