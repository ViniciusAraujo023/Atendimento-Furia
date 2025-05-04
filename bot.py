import telebot, requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('7987297251:AAECk9FEqmXncEINIKjUnwuO5hbK4opeW1w')

@bot.message_handler(content_types=['text'])
def start(msg):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Sobre nós 👥", callback_data="sobre_nos"))
    markup.add(InlineKeyboardButton("Nossa Loja 🛍️", callback_data="nossa_loja"))
    markup.add(InlineKeyboardButton("Jogos 🎮", callback_data="proximos_jogos"))
    markup.add(InlineKeyboardButton("Redes sociais 📱", callback_data="redes_sociais"))
    markup.add(InlineKeyboardButton("Canal de suporte ☎️", callback_data="canal_suporte"))
    bot.send_message(msg.chat.id, "Seja bem-vindo ao atendimento peronalizado e dedicado a CS da Fúria! Escolha uma opção:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "sobre_nos":
        bot.send_message(call.message.chat.id, "  Somos FURIA. Uma organização de esports que nasceu do desejo de representar o Brasil no CS e conquistou muito mais que isso: expandimos nossas ligas, disputamos os principais títulos, adotamos novos objetivos e ganhamos um propósito maior. Somos muito mais que o sucesso competitivo. Nossa história é de pioneirismo, grandes conquistas e tradição. \n\n🔥**VENHA FAZER PARTE DESSA NAÇÃO DE FURIOSOS**🔥")
    elif call.data == "nossa_loja":
        bot.send_message(call.message.chat.id, "Aqui está o link da nossa loja:\nhttps://www.furia.gg")
    elif call.data == "canal_suporte":
        bot.send_message(call.message.chat.id, "FAQ(loja): https://www.furia.gg/faq \nEntre em contato com nosso suporte pelo email: sac@furia.gg")
    elif call.data == "redes_sociais":
        bot.send_message(call.message.chat.id, "Siga a fúria nas redes sociais para ficar por dentro de tudo: \nInstagram: https://www.instagram.com/furiagg/ \nTwitter(X): https://x.com/FURIA \nFacebook: https://www.facebook.com/furiagg")
    if call.data == "proximos_jogos":
        bot.send_message(call.message.chat.id, "Não deixe de acompanhar os jogos do TIMÃO🔥🔥🔥 \nAcompanhe no nosso canal oficial da Twitch todos os jogos ao vivo: \n https://www.twitch.tv/furiatv \n  Ou veja o resultado diretamente pelas nossas redes sociais!!!")


bot.infinity_polling()
