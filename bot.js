const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready'. () => {
    console.log('Jestem gotowy!');
});
    
client.on('message', message => {
    if (message.content === 'ping') {
      message.reply('pong');
    }
});

// MA TAK BYC
client.login(process.env.BOT_TOKEN);
