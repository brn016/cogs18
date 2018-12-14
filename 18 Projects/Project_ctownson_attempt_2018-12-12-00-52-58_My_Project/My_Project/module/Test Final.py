#!/usr/bin/env python
# coding: utf-8

# In[16]:


from My_Functions import remove_punctuation, selector, sunlight_question, water_question, soil_question, value_question, prepare_text, end_chat, string_concatenator, list_to_string,is_in_list,find_in_list,introduction,have_a_chat


# In[31]:


assert callable(sunlight_question)
assert isinstance (sunlight_question(["sun","shine"]),str)
assert sunlight_question(["how","much","sunlight","does","my","cactus","need"])== "Cactus plants need indirect, filtered sunlight."
assert sunlight_question(["sunlight"])== "All plants need a specific amount and type of sunlight. Please specify which plant!"


# In[32]:


assert callable(water_question)
assert isinstance (water_question(["water","slide"]),str)
assert water_question(["how","often","do","i","water","my","fern"])== "Fern plants need to be watered before the soil dries, but don't let them get soggy!"
assert water_question(["water","flex","seal"])== "All plants need a specific amount of water. Please specify which plant!"


# In[33]:


assert callable(value_question)
assert isinstance (value_question(["best","fern"]),str)
assert value_question(["best","orchid","on","the","market"])== "Boat orchids are the best orchid in my opinion. They love high, bright sunlight and water every 5 to 6 days."
assert value_question(["easiest","plant","to","not","kill"])== "Succulents are the easiest plants."


# In[34]:


assert callable(soil_question)
assert isinstance (soil_question(["best","soil","for","bonsai"]), str)
assert soil_question(["best","soil","for","bonsai"])== "Bonsai plants need a mixture of 2 parts akadama, one part pumice and one part lava rock."

