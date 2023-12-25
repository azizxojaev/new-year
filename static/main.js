const envelope = document.querySelector('.envelope-wrapper');
        envelope.addEventListener('click', () => {
            envelope.classList.toggle('flap');
        });



function playAudio(){
    let audio_play = document.querySelector('#audio_play');
    audio_play.play();
}