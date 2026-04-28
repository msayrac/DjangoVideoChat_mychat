
const APP_ID = 'b7f67d03d0ce449e9970fc8e97cb6074'
const CHANNEL = 'main'
const TOKEN = '007eJxTYKisStxxtyaMb9a91EepZ6asmNPlEJChWJS564qVfBCLUrICQ5J5mpl5ioFxikFyqomJZaqlpblBWrJFqqV5cpKZgblJBPvHzIZARoYWaV9WRgYIBPFZGHITM/MYGAAYrB3n'

let UID;

// console.log('Stream.js conntected')

const client = AgoraRTC.createClient({mode: 'rtc', codec: 'vp8'});
// const client = AgoraRTC.createClient({mode: 'rtc', codec: 'vp8'});

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">My Name</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                  </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend',player)


    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])


}

joinAndDisplayLocalStream()



