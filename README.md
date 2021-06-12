# Chatbot-using-rasa

Rasa is an open source machine learning framework for building AI assistants and chatbots 

Rasa NLU — This is the place, where rasa tries to understand User messages to detect Intent and Entity in your message. Rasa NLU has different components for recognizing intents and entities, most of which have some additional dependencies.

Rasa Core — This is the place, where Rasa try to help you with contextual message flow. Based on User message, it can predict dialogue as a reply and can trigger Rasa Action Server.

This chatbot is built using rasa framework. It can be used to perform the following functions:

- provides the weather details of any city using OpenWeatherMap API
- share trending news using newsapi whenever news asks for news
- share news related to stock market
- answer some faq's related to stock market
- tell the current price of a stock any company
- It can extract and analyze the tweets related to any company and classify them into a positive or a negative tweet using 'Flair' as financial sentiment analysis allows us to understand the effect of social media reactions and emotions on the stock market and vice versa.
- It can also answer some faq's related to coronavirus
- Check the corona cases in any state of India.
- It can also check the available slots for covid vaccine on a particular date in any city by providing the pincode of that city.

Here's how the model performs after training

![Screenshot (106)](https://user-images.githubusercontent.com/62187533/121788089-1760c080-cbe8-11eb-921e-d1151e2041aa.png)
![Screenshot (107)](https://user-images.githubusercontent.com/62187533/121788081-0ca62b80-cbe8-11eb-9532-3f68d9d4f899.png)
![Screenshot (108)](https://user-images.githubusercontent.com/62187533/121788082-0e6fef00-cbe8-11eb-92a5-60654c022eb0.png)
![Screenshot (109)](https://user-images.githubusercontent.com/62187533/121788083-0fa11c00-cbe8-11eb-9593-379a86b4aebf.png)
![Screenshot (110)](https://user-images.githubusercontent.com/62187533/121788085-0fa11c00-cbe8-11eb-8c79-1194226f0f2f.png)
![Screenshot (111)](https://user-images.githubusercontent.com/62187533/121788086-1039b280-cbe8-11eb-9535-508877d507e7.png)


Using ngrok server the chatbot was deployed on telegram : https://t.me/Mydemobot20_bot

Here are some of the screenshots:

<img src="https://user-images.githubusercontent.com/62187533/121788385-85a68280-cbea-11eb-92e8-09afea8081c1.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788384-85a68280-cbea-11eb-8c54-9513506bf628.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788383-850dec00-cbea-11eb-9084-38af30685fde.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788382-83442880-cbea-11eb-9853-05ce7d3c66b7.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788438-efbf2780-cbea-11eb-8b46-25f8005b9232.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788437-efbf2780-cbea-11eb-9c03-685764e95931.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788436-edf56400-cbea-11eb-8331-6bb44e887252.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788500-50e6fb00-cbeb-11eb-9625-d88d37b89654.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788499-504e6480-cbeb-11eb-9551-09a71404c9b9.jpg" width="750" height="750">
<img src="https://user-images.githubusercontent.com/62187533/121788497-4fb5ce00-cbeb-11eb-8afe-5de9a6f3b3f0.jpg" width="750" height="750"> 
<img src="https://user-images.githubusercontent.com/62187533/121788496-4dec0a80-cbeb-11eb-82f0-2d86bb8723ab.jpg" width="750" height="750">



