import streamlit as st
import time
#    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbb      uuu      uuu             xx         xx       dddddddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu               xx     xx         ddd     ddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd        ddd
#    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbbb     uuu      uuu                  xx             ddd       ddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd      ddd
#    uuu      uuu   rrr     rrr     uuu      uuu   bbb     bbb     uuu      uuu              xx      xx         ddd     ddd
#    uuuuuuuuuuuu   rrr       rrr   uuuuuuuuuuuu   bbbbbbbbbb      uuuuuuuuuuuu             xx         xx       dddddddd



st.title("StreamLit Documentação:")


#Escolher a onde ir
with st.sidebar:

    st.markdown("# :violet[Qual parte da documentação você deseja ir?]")
    escolher = st.selectbox(
        " :red[Formas de Textos]",
        ("Nenhuma","Tilte","MarkDown","Header","Write","Badge","Caption","Code Block","Echo","Texto Perfomated","Latex","Divider")
    
    )
    escolher1 = st.selectbox(
         ":blue[Formas de Input]",
         ("Nenhuma","Button","Download button","Form Button","Link button","Page Link","Checkbox","Color Picker","Feedback","MultiSelect","Pills","Radio","Segmened Control","Select slider","Select box","Toggle","Number Input","Slider","Data Input","Time Input","Text Input","Text Area","Chat Input")
    )

#Formas de Texto    
def formasdetexto ():
    
    #Title
    if escolher == "Tilte":
    

        #Para fazer um titulo e usado o "st.tittle("Exemplo")"

        #Title explicação
        st.markdown("# :red[Titulo:]")
        st.header("Para fazer um titulo é usado o:")

        st.title(":red[Exemplo de titulo]")

        title='''Codigo:
        st.tittle('Titulo')
        '''

        st.code(title,language="python")        

    #MarkDown

    elif escolher == "MarkDown":
        #MarkDown explicação
        st.title(" :blue[MarkDown:]")
        st.header("Markdown é tipo uma forma mais facil é rapida de adicionar estilo ao texto utilizando alguns caracters especiais:")
        st.markdown("# :blue[Alguns exemplos de markwon:]")
        st.markdown(":blue[**texto em negrito por exemplo**]")
        st.markdown('#### :blue[Aumentar a fonte]')
        st.markdown('### :blue[Aumentar a fonte]')
        st.markdown('## :blue[Aumentar a fonte]')
        st.markdown('# :blue[Aumentar a fonte]')

        markdown = '''Codigo:
        st.markdown(":blue[**texto em negrito por exemplo**]")
        st.markdown('#### :blue[Aumentar a fonte]')
        st.markdown('### :blue[Aumentar a fonte]')
        st.markdown('## :blue[Aumentar a fonte]')
        st.markdown('# :blue[Aumentar a fonte]')
        '''

        st.code(markdown,language="python")


    #Header

    elif escolher =="Header":
        #Header/Subheader explicação

        st.title(" :orange[Header/Subheader]")
        st.markdown("## Um subtitulo é um subtitulo menor que pode fazer linhas como o exemplo abaixo.(unica definção que eu consegui ver).")
        st.header("Exemplo1", divider =True)
        st.header("Exemplo2", divider = True)
        st.header("Exemplo3", divider = True)
        st.header("Exemplo4", divider = True)

        header = ''' Codigo:
        st.header("Exemplo1", divider =True)
        st.header("Exemplo2", divider = True)
        st.header("Exemplo3", divider = True)
        st.header("Exemplo4", divider = True)
        '''
        st.code(header,language="python")

    #Write

    elif escolher == "Write":
        #Write Explicação

        st.title(":violet[Write]")
        st.markdown("## Você escreve normamente a letra fica pequenea.E so escrever.Assim:")
        st.write(":violet[texto dxdxdxd texto]")

        write =''' Codigo:
        st.write(":violet[texto dxdxdxd texto]")

        '''
        st.code(write,language="python")

    #Badge
    elif escolher =="Badge":
        #Badge Explicação



        st.title(":green[Badge]")
        st.markdown("## É tipo um selo,uma coisa pra se comunicar visualmente tlgd")
        st.markdown("### Tipo os exemplos abaixo:")
        st.markdown(
            ":green-badge[:material/done_all:  Feito]" \
            ":orange-badge[⚠️Urgente!]"
            ":gray-badge[🗑️Descartado]"
        )


        badge = ''' Codigo:
        st.markdown(
            ":green-badge[:material/done_all:  Feito]" \
            ":orange-badge[⚠️Urgente!]"
            ":gray-badge[🗑️Descartado]"
        )'''


        st.code(badge,language="python")

    #Caption
    elif escolher =="Caption":
            #Caption explicação
        st.markdown(
            "# :red[Caption]\n"
            "## O caption e uma pequena fonte "
        )
        st.caption("Aqui esta o teste do caption  "
            "\nO caption :blue[colorido] em **negrito** e emojis :sunglasses:"
        )

        caption ='''Codigo:
        st.caption("Aqui esta o teste do caption  "
            "\nO caption :blue[colorido] em **negrito** e emojis :sunglasses:"
        )
        '''

        st.code(caption,language="python")

    #Code Block
    elif escolher =="Code Block":
            #Caption explicação
        st.markdown(
            "# :red[Caption]\n"
            "## O caption e uma pequena fonte "
        )
        st.caption("Aqui esta o teste do caption  "
            "\nO caption :blue[colorido] em **negrito** e emojis :sunglasses:"
        )

        caption ='''Codigo:
        st.caption("Aqui esta o teste do caption  "
            "\nO caption :blue[colorido] em **negrito** e emojis :sunglasses:"
        )
        '''

        st.code(caption,language="python")

        #Code Block(Bloco com o codigo)
        st.markdown("# :blue[Code Block]"
        "\n ## O Code block e uma função que faz aparecer o codigo(utilizado para mostras os codigos anteriores)."

        )
        code = '''st.code("
        #    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbb      uuu      uuu             xx         xx       dddddddd
        #    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu               xx     xx         ddd     ddd
        #    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd        ddd
        #    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbbb     uuu      uuu                  xx             ddd       ddd
        #    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd      ddd
        #    uuu      uuu   rrr     rrr     uuu      uuu   bbb     bbb     uuu      uuu              xx      xx         ddd     ddd
        #    uuuuuuuuuuuu   rrr       rrr   uuuuuuuuuuuu   bbbbbbbbbb      uuuuuuuuuuuu             xx         xx       dddddddd

        ")
        '''

        st.code(code,language="python")


    #Echo
    elif escolher =="Echo":
        #Echo
        st.markdown("# :orange[Echo]"
            "\n ## O echo ele faz mostra o codigo e executa tipo o exemplo abaixo:")

        with st.echo():
            with st.echo():
                st.markdown("# Como diminui a fonte")  
                st.markdown("## Como diminui a fonte")  
                st.markdown("### Como diminui a fonte")  
                st.markdown("#### Como diminui a fonte")  
                st.markdown("##### Como diminui a fonte")  
                st.markdown("##### Como diminui a fonte")  
                st.markdown("###### Como diminui a fonte")  
                st.caption("Como diminui a fonte")  
            foo ='bar'
        foo='bar'

    #Texto Perfomatted

    #Perfomatted Text
    elif escolher =="Texto Perfomated":
        st.markdown(
            "# :violet[Texto Perfomatted]" \
            "\n ## O texto perfomatted eu nao etendi muito bem mas ele cria uma caixa com o comando e ele e editavel."

        )
        codigo = """
        PATO XD
        """

        st.text_area("Código Python:", codigo, height=200)

        log = """
        PATO XD
        """

        st.text_area("Log do Sistema:", log, height=150)

    #Latex
    elif escolher =="Latex":
            #latex

        st.markdown(
            "# :violet[Latex]" \
            "\n ## O latex ele faz a saida de calculos Matemáticos.Como no exemplo:"
        )

        with st.echo():

            st.latex(r'''
                b + ar + a r^2 + a l^3 + \cdots + b r^{n-1} =
                \sum_{k=0}^{n-1} cr^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
                ''')


    #Divider
    elif escolher =="Divider":
                st.markdown(
                "# :green[Divider]"
                "\n ## O divider ele divide as com linhas os texto.Por exemplo: "
            )

                with st.echo():
                    st.divider()
                    st.write("Texto uau isso e um texto")
                    st.divider()
                    st.slider("Isso e uma sla o que é",0,100, (0,25))
                    st.divider()

    #Nenhum
    elif escolher =="Nenhuma" :
        st.markdown("")

formasdetexto ()



#Formas de Input
def formasdeinput():
     
    #Button
    if escolher1 == "Button":
        st.markdown("# :red[Button]"
                    "\n ## O button cria um botão interativo")
        with st.echo():
            st.button(":red[Botão poggers]")
            st.button("Botão Xd Limão",type="secondary")
            risadinha = st.button("Botão risadinha", type="tertiary")
            st.write("Botão risadinha :", risadinha)
            if risadinha :
                st.write(":laughing:")
        foo ='bar'

    #Download Button
    elif escolher1 == "Download button":
        st.markdown("# :blue[Download Button:]"
                    "\n ## Bom e meio auto explicativo,é um botão,que faz Download")
        with st.echo():
            st.download_button(
        label="Baixar texto",
        data="Text text xd xd xdxdxd",
        file_name="Aqurivo de text.txt",
        mime="text/csv",
        icon=":material/download:",
    )
        st.markdown("#### Label = O nome que aparece no botão;"
                    "\n #### Data = O que vai ter dentro do arquivo;"
                    "\n #### File Name = Nome do arquivo quando baixar;"
                    "\n #### Mime = Tipo do arquivo"
                    "\n #### Icon = Icone do botão")
        
                    
        
    #Form button
    elif escolher1 == "Form Button":
        st.markdown("# :orange[Form Button]")
        st.markdown("## Form button é um botão que e você confirma para enfia uma informção.Como no exemplo:")
        with st.echo():
            with st.form("my form"): #Ir saber como fazer um forms
                st.form_submit_button('Botão pra atualizar') 

    #Link Button
    elif escolher1 == "Link button":
        st.markdown("# :green[Link Button]"
                    "\n ## O link button ele te redireciona para outrta pagina quando vc aperta um botão(Com um link)")
        with st.echo():
                st.link_button("Clique aqui nada suspeito","https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
                
                
    #Page link
    elif escolher1 =="Page Link":
        st.markdown("# :violet[Page Link]" \
        "\n ## Diferente do link button ele redireciona tmb so que ele consegue fazer outras abas com outros codigos")
        with st.echo():
            st.markdown("")#st.page_link("teste/lolxd.py",label="Pinto Pinto",icon="🍺")


    #Color picker
    elif escolher1 =="Color Picker":
        st.markdown("# :blue[Color Picker]"
                    "\n ## O color picker vc escolhe uma cor.È so isso ")
        with st.echo():
            
            cor = st.color_picker("Escolha uma cor")
            if cor :
                st.write("Sua cor é", cor)


    #Check box
    elif escolher1 =="Checkbox":
        st.markdown("# :orange[CheckBox]"
                    "\n ## A check box e uma caixinha que vc clica e da um ok ")
        with st.echo():
            st.write("Você consegue me ver?")
            resposta = st.checkbox("Sim")
            if resposta :
                st.write("Mentira seu but")


    #Feedback
    elif escolher1 =="Feedback":
        st.markdown("# :red[Feedback]"
                    "\n ## O feedback e um botão que vc da o feedback e ele tem dois tipos(pelo que eu vi): ")
        with st.echo():
            lugardasEstrelas =["uma","duas","três","quatro","cinco"]
            feedback = st.feedback("stars")
            if feedback is not None:
                st.markdown(f"Você selecionou  {lugardasEstrelas[feedback]} estrela(s).")


    #MultiSelect
    elif escolher1 =="MultiSelect":
        st.markdown("# :green[MultiSelect]"
                    "\n ## A multiselect e uma caixa que vc pode marcas varias coisas(Fica tipo uma lista por ordem).Tipo:")
        with st.echo():
            sucos = st.multiselect(
                "Qual é seus sucos favoritos?",
                ["Uva","Abacaxi","Limão","Laranja","Maracuja","Pessego"]
            )

            st.write("Seus sucos favoritos selecionados são: ", sucos)
            

    #Pills
    elif escolher1 =="Pills":
        st.markdown("# :violet[]")

formasdeinput ()