/**
 * for web3 1.0.0-beta.36
 * */

let fs = require("fs");
let Web3 = require('web3');

var ws_provider = 'wss://ropsten.infura.io/ws'
var web3 = new Web3(new Web3.providers.WebsocketProvider(ws_provider))

var flag1 = fs.readFileSync("flag1.txt").toString().trim();
var flag1b64 = b64encode(flag1);

if (process.argv.length != 3){
    console.error('Please provide address in ropsten. \nex. 0x4aa7c9fccf2c9082063b28cf84bf133f25f5916a');
    process.exit(1);
}
var contactAddr = process.argv[2];

function getContractInstance(jsonName, solName, contractName, contractAddr){
    let source = fs.readFileSync(jsonName+".json");
    let contracts = JSON.parse(source)["contracts"];

    let abi = JSON.parse(contracts[solName+'.sol:'+contractName]['abi']);
    let code = '0x' + contracts[solName+'.sol:'+contractName]['bin'];

    let contract = new web3.eth.Contract(abi, contractAddr);
    return contract;
}

var econtract = getContractInstance('be_owner', 'be_owner', 'be_owner', contactAddr);

console.log("Starting listner ....");



const nodeMailer = require("nodemailer");

let transporter  = nodeMailer.createTransport({
    //service: 'zoho',
    host: "smtp.buaa.edu.cn",
    secureConnection: true,
    port:465,
    auth: {
        user: 'xxx',
        pass: 'xxx'
    },  
    tls: {
	// do not fail on invalid certs
	rejectUnauthorized: false
    }
});

let defaultOptions = {
    from:'LANCTF<admin@buaa.edu.cn>',
    to:"@163.com",
    subject:"Hello",
    text:"Hello world text"
}

transporter.send = (options, to, subj, content)=>{
    // return new Promise((resolve,reject) =>{
    options['to'] = to;
    options['subject'] = subj;
    options['text'] = content;
        transporter.sendMail(options,(err,info)=>{
            if(err){
                 console.log(err)
            }
            else {
                console.log(err,info)
            }
        });
    return;
}

function b64encode(str){
    return Buffer.from(str).toString('base64');
}
function b64decode(str){
    return Buffer.from(str, 'base64').toString('ascii');
}

function emailFlag(b64email){
    //var email = b64decode(b64email);
    var email = b64email;
    //email = 'haozigege@buaa.edu.cn';
    console.log('Received SendFlag event, sending flag to ' + email);
    transporter.send(defaultOptions, email, 'Please verify your flag:', flag1b64);
}

//sendFlagEvent = econtract.events.SendFlag({fromBlock: 5147905,toBlock: 'latest'},function(error, result){
sendFlagEvent = econtract.events.SendFlag(function(error, result){
  if (result !== undefined && result !== null) {
    var args = result.returnValues;
    args["_txn"] = result.transactionHash;
    console.log('Sending Flag...');
    console.log(args);
    emailFlag(args['0'])
  }
});
