from bge import logic,events , types
import bgui
import bgui.bge_utils
import bge



#-----------------------------------------------------
from scripts.menus.libs.JSON import JsonClass
from scripts.databases.UiTextImgsData import *


import scripts.databases.globalsDatas

#-----------------------------------------------------

global_dict = bge.logic.globalDict
global_dict["INIT_GAME"] = False


global_dict                             = bge.logic.globalDict

global_dict["graphicsLights"]           = True
global_dict["graphicsShaders"]          = True
global_dict["graphicsShadows"]          = True
global_dict["graphicsRamps"]            = True
global_dict["graphicsNodes"]            = True
global_dict["graphicsExtraTextures"]    = True



#---------------
def setColorsFrames( r = 0.0 , g = 0.0  , b = 0.0  , a = 0.0 ):
    return [( r , g , b , a ) for i in range(4)] 




class MenuMainTwo(bgui.bge_utils.Layout):
    def __init__( self, sys , data ):
        super().__init__( sys , data)
        #--------------------------------
        #self.path    = bge.logic.expandPath( "//scripts/menus/image/imgs_main/" )
        self.path    = bge.logic.expandPath( "//scripts/menus/image/ui_menus/" )

        self.opsion  = bgui.BGUI_DEFAULT | bgui.BGUI_DEFAULT

        #--------------------------------
        self.text_size = 40

        
        #------- Frames -----------------

        self.MainFrame              = bgui.Frame( self , border = 0 , size = ( 1.00 , 1.00 ), pos = ( 0.0 , 0.0 )  )
        self.MainFrame.colors       = setColorsFrames( a = 0.0 )

        
        self.DownFrame              = bgui.Frame( self , border = 0 , size = ( 1.0 , 0.06 ), pos = ( 0.0 , 0.0 )  )
        self.DownFrame.colors       = setColorsFrames( a = 0.50 )

        img_button_esc = bgui.Image( self.DownFrame , self.path + "Button_esc_sair.png", size = ( 0.06 , 0.68 ), pos = ( 0.90 , 0.10 ), options = self.opsion)

        
        #---------- ELEMENTOS WIDGETS ------------------------------------------------------------------------------
        self.menu_start = self.menuStart()


        self.buttons_main = self.buttonsMenuMain()
        self.buttons_main["frame"].visible = False

        self.men_tutorial = self.menuTutorial()
        self.men_tutorial["frame"].visible = False

        self.men_opsions  = self.menuOpsions()
        self.men_opsions["frame"].visible = False

        self.men_credits  = self.menuCredits()
        self.men_credits["frame"].visible = False


        self.men_extras = self.menuExtras()
        self.men_extras["frame"].visible = False
        self.buttons_main["button_extras"]["button_image"].visible      = False
        self.buttons_main["button_extras"]["text_button"].visible       = False



        #----- ClickEvents Menu Buttons ----------------------------------------------
        self.menu_start["button_star_game"]["button_image"].on_click  = self.menuMainButtons
        self.buttons_main["button_star_game"]["button_image"].on_click  = self.menuMainButtons
        self.buttons_main["button_tutorial"]["button_image"].on_click   = self.menuMainButtons
        self.buttons_main["button_opsions"]["button_image"].on_click    = self.menuMainButtons
        self.buttons_main["button_creditos"]["button_image"].on_click   = self.menuMainButtons
        self.buttons_main["button_extras"]["button_image"].on_click     = self.menuMainButtons


        #--- Click Events Back Menus --------------------------------------------------------
        self.men_tutorial["button_voltar"]["button_image"].on_click  = self.menusBackButtons
        self.men_opsions["button_voltar"]["button_image"].on_click   = self.menusBackButtons
        self.men_credits["button_voltar"]["button_image"].on_click   = self.menusBackButtons
        self.men_extras["button_voltar"]["button_image"].on_click    = self.menusBackButtons


        #---- Menu Tuttorial Buttons events -------------------------------------------------
        self.men_tutorial["button_input_keyboard"]["button_image"].on_click  = self.menuTutorialButtons
        self.men_tutorial["button_input_joystick"]["button_image"].on_click  = self.menuTutorialButtons





        #--------------------------------------------------------------------------------------
        # Buttons Dubles menu Opsions ---------------------------------------------------------
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsLights"]          , self.dublesButtonsOpsionsMenu )
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsShaders"]         , self.dublesButtonsOpsionsMenu )
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsShadows"]         , self.dublesButtonsOpsionsMenu )
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsRamps"]           , self.dublesButtonsOpsionsMenu )
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsNodes"]           , self.dublesButtonsOpsionsMenu )
        self.setCallBacksClickDubleButtons( self.men_opsions["graphicsExtraTextures"]   , self.dublesButtonsOpsionsMenu )




        #---- MouseOvers buttons-------------------------------------------------------
        #self.manu_main["button_start"].on_hover         = self.startMouseOverButton
        
       
    

    #---------------------------------------------------------------------------------------------------

    def outTextInLines( self , text , max_size_text_line ):
        palavras    = text.split()
        linhas      = []
        linha_atual = ""

        #print( palavras )
        

        for palavra in palavras:

            if len( linha_atual) + len(palavra) + 1 <= max_size_text_line:
                linha_atual += palavra + " "

            else:
                linhas.append( linha_atual.strip())
                linha_atual = palavra + " "
        

        # Adicionar a última linha
        linhas.append( linha_atual.strip() )

        return linhas


    #---------------------------------------------------------------------------------------------------
    def buttonsImg( self , parent , sizes , positions , back_img , over_img , click_img = None , text = "" , size_text = 30 , widget_name = ""):

        return {


                "button_image"    : bgui.ImageButton(   parent , 
                                                        name            = widget_name , 
                                                        default_image   = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                        default2_image  = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                        hover_image     = ( self.path + over_img    , 1 , 1  , 1 , 1  ) ,
                                                        #click_image     = ( self.path + click_img   , 1 , 1  , 1 , 1  ) ,
                                                        size            = sizes , 
                                                        pos             = positions ,
                                                        options         = self.opsion
                                                        ),

                
                "text_button"     : bgui.Label(     parent     = parent ,
                                                    text       = text , 
                                                    pt_size    = size_text,
                                                    font       = font_texts ,
                                                    pos        = [ positions[0] + 0.02 , positions[1] + 0.01 ] ,
                                                    sub_theme  = 'Large', 
                                                    options    =  self.opsion
                                                    ),

                }


    #---------------------------------------------------------------------------------------------------
    def dubleButtonsImg( self , parent , back_img , over_img , text = "--" , size = ( 0.28 , 0.06 ) , positions = [ 0.10 , 0.25 ] , size_text = 30 , widget_button_left = "" ):
        
        #positions       = [ 0.10 , 0.25 ]
        sizes_b         = [ 0.2 , 1.0 ]
        positions_b     = [ 0.0 , 0.0 ]


        frame                = bgui.Frame( parent , border = 0 , size =  size , pos = positions  )
        frame.colors         = setColorsFrames( a = 0.50 )


        button_left          =  bgui.ImageButton(   parent          = frame  , 
                                                    name            = "left_" + widget_button_left , 
                                                    default_image   = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                    default2_image  = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                    hover_image     = ( self.path + over_img    , 1 , 1  , 1 , 1  ) ,
                                                    #click_image     = ( self.path + click_img   , 1 , 1  , 1 , 1  ) ,
                                                    size            = sizes_b  , 
                                                    pos             = positions_b ,
                                                    options         = self.opsion
                                                    )


        button_right         = bgui.ImageButton(    parent          = frame, 
                                                    name            = "right_" + widget_button_left , 
                                                    default_image   = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                    default2_image  = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                                    hover_image     = ( self.path + over_img    , 1 , 1  , 1 , 1  ) ,
                                                    #click_image     = ( self.path + click_img   , 1 , 1  , 1 , 1  ) ,
                                                    size            = sizes_b , 
                                                    pos             = [ positions_b[0] + 0.8 , positions_b[1] ]  , 
                                                    options         = self.opsion
                                                    )

        return {
                "text_view"       : bgui.Label(     parent     = parent ,
                                                    text       = text , 
                                                    font       = font_texts ,
                                                    pt_size    = 30 , 
                                                    pos        = [ positions[0] , positions[1] + 0.05 ] ,
                                                    sub_theme  = 'Large', 
                                                    options    =  self.opsion
                                                ),


                "text_center"       : bgui.Label(   parent     = frame ,
                                                    text       = "Ativado" , 
                                                    pt_size    = size_text ,
                                                    font       = font_texts ,
                                                    pos        = [ 0.3 , 0.2 ] ,
                                                    sub_theme  = 'Large', 
                                                    options    =  self.opsion
                                                ),

                "duble_buttons"     : [ button_left , button_right ] ,

                

                }


    #---------------------------------------------------------------------------------------------------
    def dubleButtonsFuncion( self , widget , set_duble_button_widget ,  names_buttons ):
        global_dict = bge.logic.globalDict

        list_states = [ "Ativado" , "Desativado" ]
        name_1      = "left_"  + names_buttons
        name_2      = "right_" + names_buttons



        if  widget.name == name_1:
            set_duble_button_widget["text_center"].text = list_states[0]
            global_dict["button_duble_start"] = True


        if  widget.name == name_2:
            set_duble_button_widget["text_center"].text = list_states[1]
            global_dict["button_duble_start"] = True


    #---------------------------------------------------------------------------------------------------
    def setCallBacksClickDubleButtons( self , duble_buttons_widget , function_call_back ):
        duble_buttons_widget["duble_buttons"][0].on_click , duble_buttons_widget["duble_buttons"][1].on_click = function_call_back , function_call_back

        pass


    #---------------------------------------------------------------------------------------------------
    def layoutMenus( self , big_frame , text_titulo_menu , text_size , text_position = [ 0.05 , 0.95 ] ):

        frame                = bgui.Frame( big_frame , border = 0 , size = ( 0.91 , 0.80 ), pos = ( 0.05 , 0.14 )  )
        frame.colors         = setColorsFrames( a = 0.50 )

        #frame_text_titulo        = bgui.Frame( frame     , border = 0 , size = ( 0.10 , 0.10 ), pos = ( 0.02 , 0.90 )  )
        #frame_text_titulo.colors = setColorsFrames( r = 0.0, g = 0.0 , b = 0.0 , a = 0.20 )
        
        frame_line_up        = bgui.Frame( frame     , border = 0 , size = ( 0.96 , 0.006 ), pos = ( 0.02 , 0.90 )  )
        frame_line_up.colors = setColorsFrames( r = 1.0, g = 1.0 , b = 1.0 , a = 1.00 )


        text_titulo_menu     = bgui.Label(  parent     = frame ,
                                            text       = text_titulo_menu , 
                                            pt_size    = text_size , 
                                            pos        = text_position ,
                                            font       = font_texts ,
                                            sub_theme  = 'Large', 
                                            options    =  self.opsion
                                            )


        pass


    def cardsConquestsExtra( self , menu_frame , conquest_true , conquest_false , true_or_false , positions , breaK_line_descritio_text = 10  , tittle_conquest = "" , conquest_descrision = [ "" , "" ] ):
        list_imagens = { "True" : str( self.path + conquest_true )  , 
                         "False": str( self.path + conquest_false )  }

        return {


                "card_1" : bgui.Image(  menu_frame , 
                                        list_imagens[ str( true_or_false ) ], 
                                        size    = ( 0.32 , 0.15 ) , 
                                        pos     = positions, 
                                        options = self.opsion
                                        ),


                "text_tittle" : bgui.Label( 
                                        parent     = menu_frame ,
                                        text       = tittle_conquest , 
                                        pt_size    = 38 , 
                                        pos        = ( 0.16 , 0.79  ) ,
                                        font       = font_texts ,
                                        sub_theme  = 'Large', 
                                        options    =  self.opsion
                                        ),


                "text_descrisions_line_1" : bgui.Label( 
                                        parent     = menu_frame ,
                                        text       = conquest_descrision[0] , 
                                        pt_size    = 31 , 
                                        pos        = ( 0.16 , 0.75  ) ,
                                        font       = font_texts ,
                                        sub_theme  = 'Large', 
                                        options    =  self.opsion
                                        ),

                "text_descrisions_line_2" : bgui.Label( 
                                        parent     = menu_frame ,
                                        text       = conquest_descrision[1] , 
                                        pt_size    = 31 , 
                                        pos        = ( 0.16 , 0.72  ) ,
                                        font       = font_texts ,
                                        sub_theme  = 'Large', 
                                        options    =  self.opsion
                                        ),


                }


        pass

    #---------------------------------------------------------------------------------------------------
    #-------- MENUS ------------------------------
    #---------------------------------------------------------------------------------------------------
    def menuStart( self ):
        frame        = bgui.Frame( self , border = 0 , size = ( 1 , 1 ), pos = ( 0 , 0 )  )
        frame.colors = setColorsFrames( a = 0.00 )

        Game_Logo    = bgui.Image( frame , self.path + "logo_game_menu.png", 
                                        size    = ( 0.38 , 0.38 ) , 
                                        pos     = ( 0.32 , 0.50 ), 
                                        options = self.opsion
                                        ),

        return { 
                "frame"    : frame ,

                "button_star_game"  : self.buttonsImg(  parent      = frame  , 
                                                sizes       = [ 0.11 , 0.04] , 
                                                positions   = [ 0.45 , 0.20 ] ,

                                                back_img    = buttons_menu_main[0][0], 
                                                over_img    = buttons_menu_main[0][1],

                                                text        = l_main[0] , 
                                                size_text   = self.text_size,
                                                widget_name = l_main[0]
                                            ),
                }


    #---------------------------------------------------------------------------------------------------
    def buttonsMenuMain( self ):
        frame        = bgui.Frame( self , border = 0 , size = ( 1 , 1 ), pos = ( 0 , 0 )  )
        frame.colors = setColorsFrames( a = 0.00 )

        frame_line_down = bgui.Frame( frame , border = 0 , size = ( 0.004 , 0.12 ), pos = ( 0.05 , 0.00 )  )
        frame_line_up   = bgui.Frame( frame , border = 0 , size = ( 0.004 , 1.0 ), pos = ( 0.05 , 0.42 )  )
        
        frame_line_down.colors  = setColorsFrames( r = 1.0, g = 1.0 , b = 1.0 , a = 1.00 )
        frame_line_up.colors    = setColorsFrames( r = 1.0, g = 1.0 , b = 1.0 , a = 1.00 )

        Game_Logo    = bgui.Image( frame , self.path + "logo_game_menu.png", 
                                        size    = ( 0.28 , 0.28 ) , 
                                        pos     = ( 0.08 , 0.65 ), 
                                        options = self.opsion
                                        ),

            

        return { 
                "frame"    : frame ,

                "button_star_game"  : self.buttonsImg(  parent      = frame  , 
                                                sizes       = [ 0.11 , 0.04] , 
                                                positions   = button_main_pos[0] ,

                                                back_img    = buttons_menu_main[0][0], 
                                                over_img    = buttons_menu_main[0][1],

                                                text        = l_main[1] , 
                                                size_text   = self.text_size,
                                                widget_name = l_main[1]
                                            ),


                "button_tutorial" : self.buttonsImg( parent      = frame  , 
                                         sizes       = [ 0.11 , 0.04] , 
                                         positions   = button_main_pos[1] ,

                                         back_img    = buttons_menu_main[0][0], 
                                         over_img    = buttons_menu_main[0][1],

                                         text        = l_main[2] , 
                                         size_text   = self.text_size ,
                                         widget_name = l_main[2]
                                    ),

                "button_opsions" : self.buttonsImg( parent      = frame  , 
                                         sizes       = [ 0.11 , 0.04] , 
                                         positions   = button_main_pos[2] ,

                                         back_img    = buttons_menu_main[0][0], 
                                         over_img    = buttons_menu_main[0][1],

                                         text        = l_main[3] , 
                                         size_text   = self.text_size,
                                         widget_name = l_main[3]
                                    ),

                "button_creditos" : self.buttonsImg( parent      = frame  , 
                                         sizes       = [ 0.11 , 0.04] , 
                                         positions   = button_main_pos[3] ,

                                         back_img    = buttons_menu_main[0][0], 
                                         over_img    = buttons_menu_main[0][1],

                                         text        = l_main[4], 
                                         size_text   = self.text_size ,
                                         widget_name = l_main[4]
                                    ),

                "button_extras" : self.buttonsImg( parent      = frame  , 
                                         sizes       = [ 0.11 , 0.04] , 
                                         positions   = button_main_pos[4] ,

                                         back_img    = buttons_menu_main[0][0], 
                                         over_img    = buttons_menu_main[0][1],

                                         text        = l_main[5] , 
                                         size_text   = self.text_size ,
                                         widget_name = l_main[5]
                                    ),

        }




     #---------------------------------------------------------------------------------------------------
   

    #---------------------------------------------------------------------------------------------------
    def menuTutorial( self ):
        big_frame            = bgui.Frame( self, border = 0 , size = ( 1.0 , 1.00 ), pos = ( 0.00 , 0.00 )  )
        big_frame.colors     = setColorsFrames( a = 0.00 )

        self.layoutMenus( big_frame , text_titulo_menu = l_main[2], text_size = 40 , text_position = [ 0.03 , 0.92 ] )


        image_keyboard_inputs  = bgui.Image(big_frame , 
                                            self.path + "tutorial_menu_keyboard_inputs.png", 
                                            size    = ( 0.78 , 0.48 ) , 
                                            pos     = ( 0.10 , 0.30 ), 
                                            options = self.opsion
                                            )

        image_joystick_inputs  = bgui.Image(big_frame , 
                                            self.path + "Tutorial_menu_joystick_inputs.png", 
                                            size    = ( 0.78 , 0.48 ) , 
                                            pos     = ( 0.10 , 0.30 ), 
                                            options = self.opsion
                                            )

        image_joystick_inputs.visible = False


        return { 

                "frame"          : big_frame ,
                
                "imagens_inputs" : [ image_keyboard_inputs , image_joystick_inputs ],

                "button_voltar"  : self.buttonsImg( parent      = big_frame , 
                                                    sizes       = [ 0.11 , 0.04] , 
                                                    positions   = buttons_manu_tutorial_pos[0] ,
                                                    back_img    = buttons_menu_main[0][0], 
                                                    over_img    = buttons_menu_main[0][1],
                                                    text        = l_main[6] , 
                                                    size_text   = self.text_size,
                                                    widget_name = l_main[6] + l_main[2]
                                                    ),


                "button_input_joystick" : self.buttonsImg(   parent      = big_frame , 
                                                             sizes       = [ 0.11 , 0.04] , 
                                                             positions   = [ 0.52 , 0.16 ] ,
                                                             back_img    = buttons_menu_main[0][0], 
                                                             over_img    = buttons_menu_main[0][1],
                                                             text        = "joystick" , 
                                                             size_text   = self.text_size,
                                                             widget_name = "button_joystick" + l_main[2]
                                                             ),


                "button_input_keyboard" : self.buttonsImg(   parent      = big_frame , 
                                                             sizes       = [ 0.11 , 0.04] , 
                                                             positions   = [ 0.36 , 0.16 ] ,
                                                             back_img    = buttons_menu_main[0][0], 
                                                             over_img    = buttons_menu_main[0][1],
                                                             text        = "keyboard" , 
                                                             size_text   = self.text_size,
                                                             widget_name = "button_keyboard" + l_main[2]
                                                             ),

                }


    #---------------------------------------------------------------------------------------------------
    def menuOpsions( self ):
        big_frame            = bgui.Frame( self, border = 0 , size = ( 1.0 , 1.00 ), pos = ( 0.00 , 0.00 )  )
        big_frame.colors     = setColorsFrames( a = 0.00 )

        self.layoutMenus( big_frame , text_titulo_menu = l_main[3], text_size = 40 , text_position = [ 0.03 , 0.92 ] )

        textsize = 30
        site_com = 0.15
        return { 

                "frame"    : big_frame ,



                "button_voltar" : self.buttonsImg(   parent      = big_frame , 
                                                     sizes       = [ 0.11 , 0.04] , 
                                                     positions   = buttons_manu_tutorial_pos[0] ,
                                                     back_img    = buttons_menu_main[0][0], 
                                                     over_img    = buttons_menu_main[0][1],
                                                     text        = l_main[6], 
                                                     size_text   = self.text_size,
                                                     widget_name = l_main[6] + l_main[3]
                                                ),

                "graphicsLights" : self.dubleButtonsImg(    parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsLights" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.70 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsLights" ),


                "graphicsShaders" : self.dubleButtonsImg(   parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsShaders" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.60 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsShaders" ),


                "graphicsShadows" : self.dubleButtonsImg(   parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsShadows" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.50 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsShadows" ),


                "graphicsRamps" : self.dubleButtonsImg(   parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsRamps" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.40 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsRamps" ),


                "graphicsNodes" : self.dubleButtonsImg(   parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsNodes" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.30 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsNodes" ),


                "graphicsExtraTextures" : self.dubleButtonsImg(   parent              = big_frame , 
                                                            back_img            = buttons_menu_main[0][0] , 
                                                            over_img            = buttons_menu_main[0][1] ,
                                                            text                = "graphicsExtraTextures" ,
                                                            size                = [ site_com , 0.04 ] ,
                                                            positions           = [ 0.07 , 0.20 ] ,
                                                            size_text           = textsize , 
                                                            widget_button_left  = "graphicsExtraTextures" ),


                }


    #---------------------------------------------------------------------------------------------------
    def menuCredits( self ):
        big_frame            = bgui.Frame( self, border = 0 , size = ( 1.0 , 1.00 ), pos = ( 0.00 , 0.00 )  )
        big_frame.colors     = setColorsFrames( a = 0.00 )

        self.layoutMenus( big_frame , text_titulo_menu = l_main[4], text_size = 40 , text_position = [ 0.03 , 0.92 ] )


        #print( l_main[5] + l_main[3] )

        return { 

                "frame"    : big_frame ,

                "button_voltar" : self.buttonsImg(   parent      = big_frame , 
                                                     sizes       = [ 0.11 , 0.04] , 
                                                     positions   = buttons_manu_tutorial_pos[0] ,
                                                     back_img    = buttons_menu_main[0][0], 
                                                     over_img    = buttons_menu_main[0][1],
                                                     text        = l_main[6], 
                                                     size_text   = self.text_size,
                                                     widget_name = l_main[6] + l_main[4]
                                                ),

                "text_credits"  : bgui.Label(   parent     = big_frame ,
                                                text       = credits_text , 
                                                pt_size    = 30 , 
                                                pos        = [ 0.15 , 0.65 ] ,
                                                sub_theme  = 'Large', 
                                                options    =  self.opsion
                                                )


                }


    #---------------------------------------------------------------------------------------------------
    def menuExtras( self ):
        #return
        global_dict         = bge.logic.globalDict
        big_frame           = bgui.Frame( self, border = 0 , size = ( 1.0 , 1.00 ), pos = ( 0.00 , 0.00 )  )
        big_frame.colors    = setColorsFrames( a = 0.00 )
        list_positions      = [ ( 0.07 , 0.68 ) , ( 0.07 , 0.52 ) , ( 0.07 , 0.36 ) , ( 0.07 , 0.20 )  ]

        self.layoutMenus( big_frame , text_titulo_menu = l_main[5], text_size = 40 , text_position = [ 0.03 , 0.92 ] )

        numb = 25 

        conquest_count = bgui.Label(    parent     = big_frame ,
                                        text       = "( " + str( numb ) + " )%" , 
                                        pt_size    = 120 , 
                                        pos        = ( 0.57 , 0.20 ) ,
                                        font       = font_texts ,
                                        sub_theme  = 'Large', 
                                        options    =  self.opsion
                                        )

        trofeu_00 = bgui.Image(  big_frame , 
                                self.path + "Trofeu_fundo.png",

                                size    = ( 0.30 , 0.40 ) , 
                                pos     = ( 0.50 , 0.40 ) , 
                                options = self.opsion
                                )


        trofeu_01 = bgui.Image(  big_frame , 
                                self.path + "Trofeu_completo_dourado.png",

                                size    = ( 0.28 , 0.37 ) , 
                                pos     = ( 0.51 , 0.42 ) , 
                                options = self.opsion
                                )




        self.cardsConquestsExtra(   menu_frame          = big_frame ,
                                    conquest_true       = "Conquista_Na_correria_True.png", 
                                    conquest_false      = "Conquista_Na_correria_False.png", 
                                    true_or_false       = False , #global_dict["Na_correria"],
                                    positions           = list_positions[0],
                                    tittle_conquest     = "Na Correria",
                                    conquest_descrision = [ "termine o jogo em menos de 1 " , "minuto e 40 segundos 0:1:40. "] 
                                )

        self.cardsConquestsExtra(   menu_frame      = big_frame ,
                                    conquest_true   = "Conquista_caçador_de_tesouro_True.png", 
                                    conquest_false  = "Conquista_caçador_de_tesouro_False.png", 
                                    true_or_false   = False , #global_dict["Caçador_de_tesouro"],
                                    positions       = list_positions[1]
                                )

        self.cardsConquestsExtra(   menu_frame      = big_frame ,
                                    conquest_true   = "Conquista_caçador_de_tesouro_True.png", 
                                    conquest_false  = "Conquista_caçador_de_tesouro_False.png", 
                                    true_or_false   = False , #global_dict["Impiedoso"],
                                    positions       = list_positions[2]
                                )

        self.cardsConquestsExtra(   menu_frame      = big_frame ,
                                    conquest_true   = "Conquista_caçador_de_tesouro_True.png", 
                                    conquest_false  = "Conquista_caçador_de_tesouro_False.png", 
                                    true_or_false   = False , #global_dict["Cansativo"],
                                    positions       = list_positions[3]
                                )


        return { 

                "frame"    : big_frame ,

                "button_voltar" : self.buttonsImg(   parent      = big_frame , 
                                                     sizes       = [ 0.11 , 0.04] , 
                                                     positions   = buttons_manu_tutorial_pos[0] ,
                                                     back_img    = buttons_menu_main[0][0], 
                                                     over_img    = buttons_menu_main[0][1],
                                                     text        = l_main[6], 
                                                     size_text   = self.text_size,
                                                     widget_name = l_main[6] + l_main[5]
                                                )
                }



    #--------- BUTTONS CALL BACKS MENUS ----------------------

    def menuMainButtons( self , widget ):
        
        #print( widget.name )

        if  widget.name == l_main[0]:
            self.buttons_main["frame"].visible = True
            self.menu_start["frame"].visible = False


        if  widget.name == l_main[1]: 
            #self.buttons_main["frame"].visible = False
            #self.menu_start["frame"].visible = False
            print( widget.name , "<------>" , l_main[1] )


        if  widget.name == l_main[2]:
            self.buttons_main["frame"].visible = False
            self.men_tutorial["frame"].visible = True


        if widget.name == l_main[3]:
            self.men_opsions["frame"].visible  = True
            self.buttons_main["frame"].visible = False


        if widget.name == l_main[4]:
            self.men_credits["frame"].visible  = True
            self.buttons_main["frame"].visible = False


        if widget.name == l_main[5]:
            self.men_extras["frame"].visible  = True
            self.buttons_main["frame"].visible = False



        pass



    def menuTutorialButtons( self , widget):
        #return
        global_dict         = bge.logic.globalDict
        #------------------------------------------
            

        if  widget.name == "button_keyboard" + l_main[2]:
            self.men_tutorial["imagens_inputs"][0].visible = True
            self.men_tutorial["imagens_inputs"][1].visible = False
            

        if  widget.name == "button_joystick" + l_main[2]:
            self.men_tutorial["imagens_inputs"][0].visible = False
            self.men_tutorial["imagens_inputs"][1].visible = True

            

        pass



    #---------
    def menusBackButtons( self , widget ):
        
        print( widget.name )

        if  widget.name == l_main[6] + l_main[2]:
            self.buttons_main["frame"].visible = True
            self.men_tutorial["frame"].visible = False


        if widget.name == l_main[6] + l_main[3]:
            self.men_opsions["frame"].visible  = False
            self.buttons_main["frame"].visible = True


        if widget.name == l_main[6] + l_main[4]:
            self.men_credits["frame"].visible  = False
            self.buttons_main["frame"].visible = True


        if widget.name == l_main[6] + l_main[5]:
            self.men_extras["frame"].visible  = False
            self.buttons_main["frame"].visible = True


        pass


    #---------
    def dublesButtonsOpsionsMenu( self , widget ):

        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsLights"] , 
                                    names_buttons           = "graphicsLights" )
        
        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsShaders"] , 
                                    names_buttons           = "graphicsShaders" )


        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsShadows"] , 
                                    names_buttons           = "graphicsShadows" )


        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsRamps"] , 
                                    names_buttons           = "graphicsRamps" )


        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsNodes"] , 
                                    names_buttons           = "graphicsNodes" )


        self.dubleButtonsFuncion(   widget , 
                                    set_duble_button_widget = self.men_opsions["graphicsExtraTextures"] , 
                                    names_buttons           = "graphicsExtraTextures" )

        pass


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


def start(cont):
    own         = cont.owner
    mouse       = bge.logic.mouse
    scene       = logic.getCurrentScene()
    global_dict = bge.logic.globalDict

    #---------------------------
    global_dict["INIT_GAME"] = False

    sy = own['sys'] = bgui.bge_utils.System('../../themes/default')
    own['sys'].load_layout( MenuMainTwo , None )

    pass



def update(cont):
    own             = cont.owner
    scene           = logic.getCurrentScene()
    global_dict     = bge.logic.globalDict
    keyboard_events = logic.keyboard.events
    mouse_events    = logic.mouse.events 
    sen , act , so  = cont.sensors , cont.actuators , scene.objects

    #------ SENSORS ---------
    #----- ACTUATORS --------
    #SetGameScene = act["SetGameScene"]
    #------ OBJECTS ---------
    #------------------------
    own['sys'].run()
    