screen_helper="""
ScreenManager:
    MenuScreen:
    UzalishajiScreen:
    UpendoScreen:
    KaziScreen:
    AmaniScreen:


<MenuScreen>:
    name:'menu'
    MDScreen:
        MDNavigationLayout:
            ScreenManager: 
                MDScreen :
                    #Now creating a box layout
                    MDBoxLayout :
                        orientation: 'vertical'
                        #Now creating a top toolbar
                        MDTopAppBar: 
                            title: 'KHLMB' #title of toolbar
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left and right action items
                            left_action_items : [['menu', lambda x : nav_drawer.set_state('toggle')]]
                            right_action_items : [['magnify', lambda x : print('serach')],['dots-vertical', lambda x : print('vertical dots')]]


                        # create the card in the middle of our top and bottom toolbars
                        # create the scrollview first


                        ScrollView:
                            #now replace our cards inside a grid layout because scrollview take only one widget
                            MDGridLayout:
                                cols : 1 #no of cols
                                size_hint_y : 1 #width of grid layout 
                                            #if you increase the number of cards then increase this value coz the size of our grid layout is fixed
                                            #so for better appearance you have to increase this value
                                #now creating our card
                                MDCard:
                                    size_hint_y: .8 #width of the card
                                    size_hint_x: .7 #length of the card

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/apples.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'                          BABA HALISI(Na Mic)'
                                            font_style:'Subtitle1'
                                            size_hint_y:None
                                            height:self.texture_size[1]

                        
                
                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/chickoo.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'Familia Ya HATUA MOJA HALISI(BABA, MAMA, HUDUMA, UDHIHIRISHO, UTIMILIFU, MWAMINIFU)'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                       


                

                        #Now creating a bottom toolbar 
                        MDBottomAppBar:
            
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left  items
                            MDTopAppBar:
                                left_action_items : [['menu', lambda x : print(menu)], ['bell', lambda x : print('Notification')], ['share-variant', lambda x : print('share')]]
                                type:'bottom' #place of toolbar
                                mode:'end' #position of root button
                                icon:'plus'
                                icon_color:[0,0,1,1]

            

            MDNavigationDrawer:
                id: nav_drawer

                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: '5dp'
                        padding: '5dp'

                        Image:
                            source:'fruits/bestpillar.jpg'

                        MDLabel:
                            text:'Nguzo Tatu Za KANISA HALISI LA MUNGU BABA'
                            font_style:'Subtitle1'
                            size_hint_y:None
                            height:self.texture_size[1]
                    
                

                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text:'Upendo Usiobagua'
                                    on_press:root.manager.current = 'upendo'                                       
                                    IconLeftWidget:
                                        icon:'handshake'
                                        on_press:root.manager.current = 'upendo'
                                OneLineIconListItem:
                                    text:'Utawala Wa Amani'
                                    on_press:root.manager.current = 'amani'
                                    IconLeftWidget:
                                        icon:'peace'
                                        on_press:root.manager.current = 'amani'
                                OneLineIconListItem:
                                    text:'Ibada ni Uzalishaji'
                                    on_press:root.manager.current = 'uzalishaji'
                                    IconLeftWidget:
                                        icon:'microphone'
                                        on_press:root.manager.current = 'uzalishaji'

                                OneLineIconListItem:
                                    text:'Kanisa Kufanya Kazi na Taifa'
                                    on_press:root.manager.current = 'kazi'
                                    IconLeftWidget:
                                        icon:'antenna'
                                        on_press:root.manager.current = 'kazi'        

                        



<UpendoScreen>:
    name:'upendo'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                
                MDScreen :
                    #Now creating a box layout
                    MDBoxLayout :
                        orientation: 'vertical'
                        #Now creating a top toolbar
                        MDTopAppBar: 
                            title: 'KHLMB' #title of toolbar
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left and right action items
                            left_action_items : [['menu', lambda x :lambda x : x]]
                            right_action_items : [['magnify', lambda x : x],['dots-vertical', lambda x : x]]


                        # create the card in the middle of our top and bottom toolbars
                        # create the scrollview first


                        ScrollView:
                            #now replace our cards inside a grid layout because scrollview take only one widget
                            MDGridLayout:
                                cols : 1 #no of cols
                                size_hint_y : 2.5 #width of grid layout 
                                            #if you increase the number of cards then increase this value coz the size of our grid layout is fixed
                                            #so for better appearance you have to increase this value
                                #now creating our card
                                MDCard:
                                    size_hint_y: .5 #width of the card
                                    size_hint_x: .7 #length of the card

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/apples.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'                          Picha ya Wahislamu'
                                            font_style:'Subtitle1'
                                            size_hint_y:None
                                            height:self.texture_size[1]

                        
                
                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/chickoo.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'                          Picha ya Mashehe'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/strawberry.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'                          Picha ya Maskofu'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                        
                                        MDRectangleFlatButton:
                                            text:'Nyuma'
                                            pos_hint: {'center_x':0.85,'center_y':0.01}
                                            on_press:root.manager.current = 'menu'
                       


                

                        #Now creating a bottom toolbar 
                        MDBottomAppBar:
            
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left  items
                            MDTopAppBar:
                                left_action_items : [['arrow-left', lambda x : x], ['bell', lambda x : x]]
                                type:'bottom' #place of toolbar
                                mode:'end' #position of root button
                                icon:'plus'
                                icon_color:[0,0,1,1]


<AmaniScreen>:
    name:'amani'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                
                MDScreen :
                    #Now creating a box layout
                    MDBoxLayout :
                        orientation: 'vertical'
                        #Now creating a top toolbar
                        MDTopAppBar: 
                            title: 'KHLMB' #title of toolbar
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left and right action items
                            left_action_items : [['menu', lambda x :lambda x : x]]
                            right_action_items : [['magnify', lambda x : x],['dots-vertical', lambda x : x]]


                        # create the card in the middle of our top and bottom toolbars
                        # create the scrollview first


                        ScrollView:
                            #now replace our cards inside a grid layout because scrollview take only one widget
                            MDGridLayout:
                                cols : 1 #no of cols
                                size_hint_y : 2.5 #width of grid layout 
                                            #if you increase the number of cards then increase this value coz the size of our grid layout is fixed
                                            #so for better appearance you have to increase this value
                                #now creating our card
                                MDCard:
                                    size_hint_y: .5 #width of the card
                                    size_hint_x: .7 #length of the card

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/cherry.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Dodoma ya kuombea Amani'
                                            font_style:'Subtitle1'
                                            size_hint_y:None
                                            height:self.texture_size[1]

                        
                
                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/watermelon.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada iliyofuta Korona'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/mango.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada iliyofuta Ebola Mwanza'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                        
                                        MDRectangleFlatButton:
                                            text:'Nyuma'
                                            pos_hint: {'center_x':0.85,'center_y':0.01}
                                            on_press:root.manager.current = 'menu'
                       


                

                        #Now creating a bottom toolbar 
                        MDBottomAppBar:
            
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left  items
                            MDTopAppBar:
                                left_action_items : [['arrow-left', lambda x : x], ['bell', lambda x : x]]
                                type:'bottom' #place of toolbar
                                mode:'end' #position of root button
                                icon:'plus'
                                icon_color:[0,0,1,1]

<UzalishajiScreen>:
    name:'uzalishaji'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                
                MDScreen :
                    #Now creating a box layout
                    MDBoxLayout :
                        orientation: 'vertical'
                        #Now creating a top toolbar
                        MDTopAppBar: 
                            title: 'KHLMB' #title of toolbar
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left and right action items
                            left_action_items : [['menu', lambda x :lambda x : x]]
                            right_action_items : [['magnify', lambda x : x],['dots-vertical', lambda x : x]]


                        # create the card in the middle of our top and bottom toolbars
                        # create the scrollview first


                        ScrollView:
                            #now replace our cards inside a grid layout because scrollview take only one widget
                            MDGridLayout:
                                cols : 1 #no of cols
                                size_hint_y : 3.0 #width of grid layout 
                                            #if you increase the number of cards then increase this value coz the size of our grid layout is fixed
                                            #so for better appearance you have to increase this value
                                #now creating our card
                                MDCard:
                                    size_hint_y: .5 #width of the card
                                    size_hint_x: .7 #length of the card

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/dragon fruit.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Picha za Uzao wote wanaozalisha'
                                            font_style:'Subtitle1'
                                            size_hint_y:None
                                            height:self.texture_size[1]

                        
                
                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/grapes.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Uzalishaji Moyo Moja'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/apples.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Uzalishaji Arusha'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/pomegranate.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Uzalishaji Tanga'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/chikoo.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Uzalishaji Jombe'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/strawberry.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Uzalishaji Iringa'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                        
                                        MDRectangleFlatButton:
                                            text:'Nyuma'
                                            pos_hint: {'center_x':0.85,'center_y':0.01}
                                            on_press:root.manager.current = 'menu'
                       


                

                        #Now creating a bottom toolbar 
                        MDBottomAppBar:
            
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left  items
                            MDTopAppBar:
                                left_action_items : [['arrow-left', lambda x : x], ['bell', lambda x : x]]
                                type:'bottom' #place of toolbar
                                mode:'end' #position of root button
                                icon:'plus'
                                icon_color:[0,0,1,1]


<KaziScreen>:
    name:'kazi'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                
                MDScreen :
                    #Now creating a box layout
                    MDBoxLayout :
                        orientation: 'vertical'
                        #Now creating a top toolbar
                        MDTopAppBar: 
                            title: 'KHLMB' #title of toolbar
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left and right action items
                            left_action_items : [['menu', lambda x :lambda x : x]]
                            right_action_items : [['magnify', lambda x : x],['dots-vertical', lambda x : x]]


                        # create the card in the middle of our top and bottom toolbars
                        # create the scrollview first


                        ScrollView:
                            #now replace our cards inside a grid layout because scrollview take only one widget
                            MDGridLayout:
                                cols : 1 #no of cols
                                size_hint_y : 2.8 #width of grid layout 
                                            #if you increase the number of cards then increase this value coz the size of our grid layout is fixed
                                            #so for better appearance you have to increase this value
                                #now creating our card
                                MDCard:
                                    size_hint_y: .5 #width of the card
                                    size_hint_x: .7 #length of the card

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/apples.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Kufufua Utalii Ukanda wa Kaskazini'
                                            font_style:'Subtitle1'
                                            size_hint_y:None
                                            height:self.texture_size[1]

                        
                
                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/grapes.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Kasemehe bure Korona'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/watermelon.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Shukrani Baada ya Korona Kufutika'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                MDCard:
                                    size_hint_y: .7
                                    size_hint_x: .7 

                                    #creating a box layout
                                    MDBoxLayout:
                                        orientation:'vertical'
                                        padding:'2dp'
                                        spacing:'2dp'

                                        #Adding Image
                                        Image:
                                            source:'fruits/mango.jpg'

                                        #writting name of fruit
                                        MDLabel:
                                            text:'      Ibada ya Kufuta Teleza Kigoma'
                                            font_style:'Subtitle1'
                                            size_hint_y: None
                                            height:self.texture_size[1]

                                        
                                        MDRectangleFlatButton:
                                            text:'Nyuma'
                                            pos_hint: {'center_x':0.85,'center_y':0.01}
                                            on_press:root.manager.current = 'menu'
                       


                

                        #Now creating a bottom toolbar 
                        MDBottomAppBar:
            
                            md_bg_color: [0,0,1,1] #background color of toolbar
                            #Adding left  items
                            MDTopAppBar:
                                left_action_items : [['arrow-left', lambda x : x], ['bell', lambda x : x]]
                                type:'bottom' #place of toolbar
                                mode:'end' #position of root button
                                icon:'plus'
                                icon_color:[0,0,1,1]













       

"""