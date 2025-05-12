import streamlit as st
import pandas as pd
import datetime
import numpy as np

st.set_page_config(page_icon="🧾",page_title="Documentação : ")
st.title("StreamLit Documentação:")

#    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbb      uuu      uuu             xx         xx       dddddddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu               xx     xx         ddd     ddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd        ddd
#    uuu      uuu   rrrrrrrrrr      uuu      uuu   bbbbbbbbbbb     uuu      uuu                  xx             ddd       ddd
#    uuu      uuu   rrr    rrr      uuu      uuu   bbb     bbb     uuu      uuu                xx  xx           ddd      ddd
#    uuu      uuu   rrr     rrr     uuu      uuu   bbb     bbb     uuu      uuu              xx      xx         ddd     ddd
#    uuuuuuuuuuuu   rrr       rrr   uuuuuuuuuuuu   bbbbbbbbbb      uuuuuuuuuuuu             xx         xx       dddddddd


#Escolher a onde ir
with st.sidebar:

    

    st.markdown("# :violet[Qual parte da documentação você deseja ir?]")
    escolher = st.selectbox(
        " :red[Formas de Textos]",
        ("Nenhuma","Title","MarkDown","Header","Write","Badge","Caption","Code Block","Echo","Texto Perfomated","Latex","Divider")
    
    )
    escolher1 = st.selectbox(
         ":blue[Formas de Input]",
         ("Nenhuma","Button","Download button","Form Button","Link button","Page Link","Checkbox","Color Picker","Feedback","MultiSelect","Pills","Radio","Segmened Control","Select slider","Select box","Toggle","Number Input","Slider","Data Input","Time Input","Text Input","Text Area","Chat Input")
    )

    escolher2 = st.selectbox(
        ":orange[Formas de Elementos de Midia]",
        ("Nenhuma","Image","Logo","Audio","Video")
    )
    escolher3 = st.selectbox(
        ":green[Formas de Layouts and Containers]",
        ("Nenhuma","Colunas","Container","Modal Dialog","Empty","Expander","Popover","Sidebar","Tabs")
    )


#Formas de Texto    
def formasdetexto ():
    
    #Title
    if escolher == "Title":
    

        #Para fazer um titulo e usado o "st.tittle("Exemplo")"

        #Title explicação
        st.markdown("# :red[Titulo:]")
        st.header("Para fazer um titulo é usado o:")

        st.title(":red[Exemplo de titulo]")

        title='''Codigo:
        st.title('Titulo')
        '''

        st.code(title,language="python")        

    #MarkDown

    elif escolher == "MarkDown":
        #MarkDown explicação
        st.title(" :blue[MarkDown:]")
        st.header("Markdown é tipo uma forma mais facil é rapida de adicionar estilo ao texto utilizando alguns caracters especiais:")
        st.markdown("# :blue[Alguns exemplos de markdown:]")
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

    #Perfomatted Text
    elif escolher =="Texto Perfomated":
        st.markdown(
            "# :violet[Texto Formatado]" \
            "\n ## O texto perfomatted eu nao etendi muito bem mas ele cria uma caixa com o comando e ele e editavel."

        )
        codigo = """
        🐣Piu!!!
        """

        st.text_area("Código Python:", codigo, height=200)

        log = """
        🐤Piu Piu!!!
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
                    st.slider("Escolha um número",0,100, (0,25))
                    st.divider()

    #Nenhum
    elif escolher =="Nenhuma" :
        st.markdown("")

formasdetexto ()

st.markdown("---")

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
        "\n ## Diferente do link button ele redireciona tmb so que ele consegue fazer outras abas com outros codigos:")

        st.markdown("#### Obs:Sempre crie a uma pasta chamada 'pages' desse jeito e coloque o arquivos para fazer outra pagina")

        pagelink = '''
            st.page_link("outra_pagina.py", label="Pagina Ota", icon="🐜")
            '''

        st.code(pagelink,language="Python")


    #Color pickerSA
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
                st.write("Não consegue não XD🤯")


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
        st.markdown("# :violet[Pills]"
                    "\n## Esse input cria uma caxinha que poder ser selecionada.A caxinha e em forma de pilulas(Por isso o nome 'Pills')")
        with st.echo():
            a = "a"
            #De Foma Multi(Varias podem ser selecionada):
            op = ["Norte", "Sul", "Leste", "Oeste"]
            selecionar = st.pills("Direções", op,selection_mode="multi")
            st.markdown(f"Opções selecionadas: {selecionar}")
            #De Fomma Single(So uma pode ser selecionada):
            op2 = ["🍗", "🍪", "🥓", "🍜","🍧","🥨","🍣","🍫"]
            selecionar2 = st.pills("Escolha uma comida : ", op2,selection_mode="single")
            st.markdown(f"Sua comida escolhida é : {selecionar2}")

    #Radio
    elif escolher1 =="Radio":
        st.markdown("# :red[Radio]"
                    "\n ## Cria um botão de seleção onde o usuário só pode escolher uma opção de uma lista.\n ## É como aqueles botões redondos que você vê em formulários web — só dá pra marcar uma por vez.")
        with st.echo():
            escolha = st.radio(
                "Escolha um cantor",
                ["Gustavo Lima","Michael Jackson","Bermas da Segunda Guerra"]
            )        
            st.markdown(f"## :rainbow[Você escolheu o: {escolha}]")

    #Segmented Control
    elif escolher1 =="Segmened Control":
        st.markdown("# :blue[Segemened Control]"
                    "\n ## É um componente do Streamlit que cria um controle de opções segmentadas —parecido com abas, mas em formato de botões “lado a lado”.")
        

        st.markdown("## Escolha de um dos Personagens : ")
        ota = st.segmented_control(
            "",
            ["🍻Bermas","🍺Frank","🍭Davi"]
        ) 
        st.markdown(f"## :rainbow[Você escolheu o: {ota}]")

    #Select SLider
    elif escolher1 =="Select slider":
        st.markdown("# :red[Select slider]"
                    "\n ## É um :red[***Slider de seleção***] que permite escolher um valor (ou intervalo) de uma lista de opções")
        with st.echo():
            st.markdown("## Escolha a dificuldade:")
            difi = st.select_slider(
                "",
                ["Fácil","Medio","Dificil"]
            )
            st.markdown(f"## Dificuldade escolhida foi : {difi}")

    #Select Box 
    elif escolher1 =="Select Box":
        st.markdown("# :green[Select Box]"
                    "\n ## Permite o usuário escolher uma opção de uma lista suspensa.")
        with st.echo():
            st.markdown("## Escolha sua fruta favorita")
            fruta = st.selectbox(
                ["Maça","Banana","Laranja","Morango"]
            )
            st.markdown(f"## Sua fruta favorita é : {fruta}")

    #Toggle
    elif escolher1 =="Toggle":
        st.markdown("# :violet[Toggle]"
                    "\n ## O toggle é um botão de ligar/desligar")
        with st.echo():
            modo = st.toggle("Ativar Modo Noturno?")
            if modo:
                st.markdown("#### Modo Noturno ativado🌙")
            else:
                st.markdown("#### Modo Noturno Desligado ☀")

    #Number Input
    elif escolher1 =="Number Input":
        st.markdown("# :orange[Number Input]"
                    "\n ## Permite o usuário digitar ou escolher um número dentro de um intervalo.")
        with st.echo():
            st.markdown("### Digite um numero :")
            numero = st.number_input("", min_value=0, max_value=100)
            st.markdown(f"### O numero digitado foi : {numero}")           

    #Slider 
    elif escolher1 =="Slider":
        st.markdown("# :blue[Slider]"
                    "\n ## É aquele controle deslizante que você arrasta para escolher um valor numérico.")
        with st.echo(): 
            st.markdown("#### Escolha um valor : ")
            valor = st.slider (" ",0,100,50)
            st.markdown(f"Valor escolhido foi : {valor}")

    #Date Input
    elif escolher1 =="Data Input":
        st.markdown("# :red[Data Input]"
                    "\n ## Um calendário para o usuário escolher uma data.")
        with st.echo():
            st.markdown("#### Escolha Uma Data : ")
            data = st.date_input(" ", datetime.date.today())
            st.markdown(f"#### A Data escolhida foi : {data}")
            tay = datetime.date(2008,12,2)
            if data == tay:
                st.markdown("## O dia que o amor da minha vida nasceu ❤")

    #Time input
    elif escolher1 =="Time Input":
        st.markdown("# :violet[Time Input]"
                    "\n ## Permite o usuário escolher uma hora.")
        with st.echo():
            st.markdown("#### Escolha um horario :")
            tempo = st.time_input(" ",datetime.time(12,0,0 ))
            st.markdown(f"#### O horario escolhido foi : {tempo}")

    #Text input
    elif escolher1 =="Text Input":
        st.markdown("# :orange[Text Input]"
                    "\n ## Caixinha simples de texto, onde o usuário digita algo.")
        with st.echo():
            st.markdown("Qual é o seu nome? ")
            nome = st.text_input("")
            st.markdown(f"Olá, {nome}! Tudo Bem?")

    #Text Area
    elif escolher1 =="Text Area":
        st.markdown("# :red[Text Area]"
                    "\n ## Uma caixona de texto para escrever textos maiores.")
        with st.echo():
            st.markdown("#### Digite qualquer coisa : ")
            blabla = st.text_area("")
            st.markdown(f"#### Vc digitou {blabla}")

    #Chat Input
    elif escolher1 =="Chat Input":
        st.markdown("# :blue[Chat Input]"
                    "\n ## Uma caixinha para entrada de texto parecida com chat.")
        with st.echo():
            msg = st.chat_input("Digite sua mensagem")
            if msg:
                st.write(f"A mensagem que você escreveu foi: {msg}")

formasdeinput ()

st.markdown("---")

#Formas de Midia
def formasmidia():
    
    #Imagem
    if escolher2 =="Image":
        st.markdown("# :red[Image]" \
        "\n ## Cria uma imagem.Pode ser por arquivo baixado ou por link")
        with st.echo():
            st.image("https://sistemafieto.com.br/gestor/Repositorio/CRP.Sistema.PortalSistemaFIETO.SENAI.CursoSenai/638629619017479512.png")
        st.markdown("#### Ou da pra fazer de outro jeito:")
        with st.echo():
            st.image("senai.png")
    
    #Logo
    elif escolher2 =="Logo":
        st.markdown("# :blue[Logo]" \
        "\n ## Cria uma logo que fica no lado esquerdo superior")
        logo = '''logo = "https://sua-logo.com"
            \nlogolocal = "logo.png"
            \nst.logo(logo)
            \nst.logo(logolocal)'''
        st.code(logo,language="python")
            

    #Audio
    elif escolher2 =="Audio":
        st.markdown("# :orange[Audio]"
                    "\n ## Cria um audio que se possa escutar dentro do site:")
        with st.echo():
            audio=("https://cdn.discordapp.com/attachments/1126193178295423057/1366167618926542939/Syn_Cole_-_Feel_Good__Future_House__NCS_-_Copyright_Free_Music.mp3?ex=680ff63e&is=680ea4be&hm=664f3a5c8cd14a57e2509d63b0c7e55c4b2b6dd054da7bcb51291587bcfbf74b&")
            st.audio(audio)

    #Video
    elif escolher2 =="Video":
        st.markdown("# :green[Video]"
                    "\n ## Cria um video dentro do site:")
        with st.echo():
            video=("https://www.youtube.com/watch?v=di-itvdeoKI")
            st.video(video)

st.markdown("---")
formasmidia()
#Formas de Layouts e Containers
def formaslayouts():

    #Colunas
    if escolher3 == "Colunas":
        st.markdown("# :red[Colunas(Columns)]"
                    "\n ## Divide na pagina colunas verticais(quantas vc quiser)")
        
        with st.echo():
            col1,col2,col3,col4 = st.columns(4)
            with col1:
                
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col2:
               
                st.image("https://static.streamlit.io/examples/dog.jpg")
            with col3:
                
                st.image("https://static.streamlit.io/examples/owl.jpg")
            with col4:
                st.image("https://static.streamlit.io/examples/owl.jpg")

    #Container
    elif escolher3 =="Container":
        st.markdown("# :blue[Container]"
                    "\n ## Cria uma caixa onde tudo feito nela.Fica dentro dela")
        
        with st.container():
            st.write("Aqui fica dentro")

            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

            st.bar_chart(chart_data)

        st.write("Aqui fica fora")

    
    elif escolher3 == "Modal Dialog":
        st.markdown("# :orange[Modal Dialog]"
                    "\n ## É uma janela temporária que aparece no meio da tela, escurecendo o resto do app (igual a um alerta em apps de celular")
        with st.echo():
            @st.dialog("Cast your vote")
            def vote(item):
                st.write(f"Why is {item} your favorite?")
                reason = st.text_input("Because...")
                if st.button("Submit"):
                    st.session_state.vote = {"item": item, "reason": reason}
                    st.rerun()

            if "vote" not in st.session_state:
                st.write("Vote for your favorite")
                if st.button("A"):
                    vote("A")
                
            else:
                f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}" 
                            
formaslayouts()

#Final
st.markdown("---")

    
