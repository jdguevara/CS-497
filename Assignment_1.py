
# coding: utf-8

# <html>
#     <h5>Jaime Guevara<br/>
#         CS-497 Spring 2019<br/>
#         01/14/2019
#         <br/>
#         Assignment 1 Questions:
#     </h5>
#     <ol>
#         <li><strong>Name:</strong><br/>Jaime Guevara</li>
#         <li><strong>Planned graduation date:</strong><br/>December 2019</li>
#         <li><p><strong>What are your plans for after graduation?</strong><br/>&emsp;I'd like to go into industry, not sure what field just yet (though I have enjoyed Web Dev and Software Engineering so far), but I'm open to anything. Eventually down the road I'd like to get a PhD. but since I'm still not sure as to what I'd like to focus on I will leave that after I've built up my skills more through hands-on industry experience.</p></li>
#         <li><p><strong>Why did you sign up for this class?</strong><br/>&emsp;I think it's an interesting topic, and if I can get more knowledge of this particular CS area and at the same time knock out some credit for my degree then all the better. Also the lab that I currently work in does Machine Learning on Organic Photovoltaics, but they use random forests and I thought learning about another aspect of Machine Learning (such as Neural Networks) might be a neat thing to do.</p></li>
#         <li><p><strong>What are some things you hope to learn from this class?</strong><br/>&emsp;More about Neural Networks and Machine Learning models/algorithms in general<p></li>
#         <li><p><strong>What other classes or experiences do you have with machine learning?</strong><br/>&emsp;None from myself (at least not building models for ML) but I have read some of the literature from work and it seems like really fascinating stuff.</p></li>
#     </ol>
# </html>

# In[7]:


# Import shuffle from the random module
from random import shuffle

# Creating a list in Python
names = ["Bob", "Alex", "Daniele", "Austin", "Sara", "Jon", "Matty"]

# Integer that defines the max size of groups allowed to be formed
max_size = 2

# The function we want: it takes in a name list, and a max group size. 
def shuffle_groups(name_list, max_group_size):
    """
    
    """
    # We shuffle the names prior, as shuffling them during iteration may cause duplicates
    shuffle(name_list) 
    # Iterate over the list, incrementing based on our group size (i.e. our step-size)
    for i in range(0, len(name_list), max_group_size):
        group = name_list[i:i+max_group_size]
        # If we've met our group size goal yield a group as a tuple
        if len(group) == max_group_size: 
            yield tuple(group)
        # It takes the remaining names in the list
        elif len(name_list) - i < max_size:
            group = name_list[i:len(name_list)] 
            yield tuple(group)

# List out the groups, but assign them to a variable to be used later/printed
group_list = list(shuffle_groups(names, max_size)) 

# Print out the group list
print(group_list)

