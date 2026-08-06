const sendBtn = document.getElementById("send-btn");
const inputBox = document.getElementById("question");
const chatBody = document.getElementById("chat-body");

sendBtn.addEventListener("click", sendMessage);

inputBox.addEventListener("keypress", function(e){
    if(e.key==="Enter"){
        sendMessage();
    }
});

function sendMessage(){

    let message = inputBox.value.trim();

    if(message==="") return;

    // User message
    chatBody.innerHTML += `
    <div class="user-message">
        <div class="message">
            ${message}
        </div>
    </div>
    `;

    inputBox.value="";

    fetch("/get",{
        method:"POST",
        headers:{
            "Content-Type":"application/x-www-form-urlencoded"
        },
        body:"msg="+encodeURIComponent(message)
    })
    .then(response=>response.text())
    .then(data=>{

        chatBody.innerHTML += `
        <div class="bot-message">

            <div class="bot-icon">
                <i class="fa-solid fa-stethoscope"></i>
            </div>

            <div class="message">
                ${data}
            </div>

        </div>
        `;

        chatBody.scrollTop=chatBody.scrollHeight;
    })
    .catch(error=>console.log(error));
}