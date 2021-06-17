### Resolved: `discord.errors.LoginFailure: Improper token has been passed.`

## A new method of gaining User Token
I resoved this issue by using another method of gaining the User Token.
## Tested using: 
* Google Chrome 91.0.4472.106 
*  Windows 10 Home 

## Straight-forward tutorial
https://user-images.githubusercontent.com/21064622/122353789-1073de00-cf59-11eb-945d-31557a029423.mp4


## Procedure in details
1. Create a new Discord User
2. While in the https://discord.com/channels/@me
3. Open Developer Tools (F12)
   1. Open `Application` Tab
   2. Choose `Local Storage` Tab
   3.  **Toggle `Device Tool Bar`(This is important)**
   4. Type `token` inside `Filter` input 
   5. Look for a `Key` equal to `token`
     The `Value` is the **User Token**.
4. Example of User Token:  `"ODU0OTY2MDA1MjM0NTMyMzcy.YMroGw.dqpvEMtB2V4dZRNX3WjAPjpz4PU"` 
5. Remember to remove quotes before usage: `ODU0OTY2MDA1MjM0NTMyMzcy.YMroGw.dqpvEMtB2V4dZRNX3WjAPjpz4PU`

Original Source: https://pcstrike.com/how-to-get-discord-token/

