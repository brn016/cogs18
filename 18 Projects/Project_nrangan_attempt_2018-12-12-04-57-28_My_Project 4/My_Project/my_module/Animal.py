# A4 assignment Cat class with more attributes which are used 
# to make the cats interact, eat, and move differently on the board 
class Animal():
    def __init__(self, character=8982,name='Animal'):
        self.character=chr(character)
        self.position= [0,0]
        self.moves=[[-1,0],[1,0],[0,1],[0,-1]]
        self.grid_size= None
        self.fight= [['Bite'],['Scratch']]
        self.fight_move= 'Bite'
        self.name= name
        self.food_coordinate= None
        self.fight_list= None
        self.fight_count= None
        self.position_list= None
        self.position_in_list=None
        self.eaten= False

"" this is a much more modified version of bots from A4, the only parts that are the same
are some instance attributes, move(). However cat_move_help has components of A4 wander, 
but modified according to the project""
class Cat(Animal):
    
    def __init__(self, character=8982,name='Cat'):
        super().__init__(character, name)

        self.moves=[[-1,1],[1,1],[1,-1],[-1,-1],[-1,0],[1,0],[0,1],[0,-1]]
        
          
    # how the cat will move throughout the board 
    # should check previous position- and determine the next step
    #cat should try and move in + movement
    #Information: Bite beats scratch. 
  
    def fight1(self):
        #Cat can only Bite and Scratch      
        list_to_return=[]
        if self.fight_count==0 or 2:
            self.fight_count=0  
        fight_move= self.fight[self.fight_count]            
        if self.fight_list!=[]:
           # go through fight list 
            for i in range(len(self.fight_list)):
                if self.fight_list[i] != fight_move:
                    # which ever one loses, the position is put on the list        
                    if self.fight_list[i]== 'Scratch':
                        #fight_move must be Bite which kills scratch 
                        list_to_return.append(self.position_list[i])
                        # only one element should be on the list
                        return list_to_return 
                    elif self.fight_list[i]=='Bite':
                        #fight_move must be Scratch which loses 
                        self.position_list[i]= self.position_in_list
                        list_to_return.append(self.position_list[i])
                        return list_to_return 
        #change the count so next time, the attack changes
        self.fight_count= self.fight_count+1
 		#return the list of who won
        return list_to_return
           
    #checks to see if eaten. play_board function determines if true or false 
    #and put back here 
    def eat(self):
        self.eaten= True
        
     
    # this method, manipulates it's moves when it has eaten
    def cat_move_help(self):
        has_new_pos= False
        while not has_new_pos:
            if self.eaten==True:
                move= random.choice(self.moves)*2
            else:
                move= random.choice(self.moves)
            new_pos=add_lists(self.position, move)
            has_new_pos= check_bounds(new_pos, self.grid_size)
            
        return new_pos
    
    def move(self):
        self.position= self.cat_move_help()