from utils import Utils
import openai

keys = Utils.read_keys()

openai.api_key = keys["OPENAI_API_KEY"]

reviews = [
    "!Muy delicioso!! En todos. Small bites, but adequate for me.<br>Service was attentive. Atmosphere is energetic verging on loud. Still, table seating is intimate enough that conversations are not hindered."
    ,"suerte! this place has been on my list for sooo long and i finally got to try it!!! it&#39;s family style so we just ordered a bunch of dishes <br><br>- fried summer squash w basil crema: 7/10 so good but too salty<br>- lentil crema dip 9/10 loved the concept and flavor, also the tortillas were so thick it was incredible<br>- mushroom chorizo tartes 3/10 did not enjoy these<br>- pesto tamal: 9/10, loved the texture and flavor. was $19 for one singular tamal but it was soooo good<br>- peach tres leches cake: 10/10 sooooo good the flavor was immaculate. one of the best desserts i&#39;ve had in a while"
    ,"Suadero tacos will forever be the greatest taco in Texas. Amazing food and drinks. Sitting at the bar is a lot of fun and great vibe."
    ,"Had a great dinner here last night. Food was incredible - reccomend the esquires, tacos, and duck although everything coming out looked amazing! The service was also fantastic. We had a reservation and they were behind but that&#39;s not surprising for a holiday weekend. They were so sweet and kept us updated the entire time. They also comped part of the bill and the manager came out to apologize. They went above and beyond what I would have expected and despite the delay would definetly dine again."
    ,"Food was great but the service wasn&#39;t the best and the food was overly priced with really small portions. Don&#39;t think it&#39;s worth coming back."
    ,"First time visiting Suerte. I cannot believe it&#39;s been 5 years since they opened and we finally made it. The whole vibe is great. Ambiance, great service by Lucas and the Suadero tacos are a must. Just order 2 orders for the table, seriously you won&#39;t regret it. We always start dinner with dessert, chaco taco and chocolate tres leches first (don&#39;t knock it until you try it) and we tried a little of everything. The calabaza in butternut squash mole is liffeeeee. Like how do they do it. Bringing so many flavors to calabaza?!? Cabrito y carnitas were a table favorite too! I can&#39;t wait to go back and try the cerviche. Make a reservation on a Monday night, it&#39;s the night to be out. Ask to be seated in Lucas&#39;s section and he&#39;ll make it memorable. I love a great staff that knows the menu front and back and especially how dishes are prepared. Chefs kiss y&#39;all!<br>Food: 5/5  |  Service: 5/5  |  Atmosphere: 5/5"
    ,"Excellent <br>Expensive <br>Food was good<br>Drinks were good <br>Make reservations <br>California has better"
    ,"The service was great but the food and drinks were just okay. Great location and vibes though!"
    ,"My recent visit to Suerte was an absolute disaster from start to finish. I&#39;ve never felt more insulted and mistreated at a dining establishment in my life. The reason? The staff claimed we were intoxicated and refused to serve us, an accusation that couldn&#39;t have been further from the truth.<br><br>It&#39;s shocking that a restaurant would make such baseless assumptions about their customers. Not only were we completely sober, but the manner in which we were approached was incredibly condescending and humiliating. Instead of being welcomed, we were met with suspicion and disdain.<br><br>What&#39;s truly disappointing is that we were looking forward to trying the food and experiencing the ambiance that Suerte had to offer. However, we were denied that opportunity due to the staff&#39;s unfair and discriminatory behavior. This incident has left me not only frustrated but deeply saddened by the lack of professionalism and respect shown by the staff.<br><br>I implore anyone reading this review to think twice before giving Suerte your business. No customer should ever be subjected to the kind of treatment we received. It&#39;s disheartening to think that such behavior is tolerated in any establishment. My friends and I will certainly never set foot in this restaurant again, and I hope others take heed and avoid this disappointing experience."
    ,"The hostesses were extremely unwelcoming, we had 2 reservations for 2 groups of 6 people. They accused one of the members of our group (who&#39;s a lively individual) of being intoxicated (which was extremely hurtful, as he has been 7 years sober) therefore canceling both reservations and asking us to leave. The whole interaction felt quite discriminatory as our group was racially mixed. Needless to say we will not be recommending Suerte to any of our friends and family."
]


prompt_to_chatgpt = [
  {
    "role": "system",
    "content": Utils.read_prompt()
  }
]
for review in reviews:
  prompt_to_chatgpt.append(
    {      
      "role": "user",
      "content": review
    }
  )

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=prompt_to_chatgpt,
  temperature=0.02,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print('--')
print(response["choices"][0]["message"]["content"])
print('--')
