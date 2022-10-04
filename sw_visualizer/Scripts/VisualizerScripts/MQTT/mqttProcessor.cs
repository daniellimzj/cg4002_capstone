using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.UI;

public class mqttProcessor : MonoBehaviour
{

    public UI_Manager ui_manager;
    public AR_Manager ar_manager;

    string test_msg = @"[{""p1"": {""hp"": 30, ""action"": ""grenade"", ""bullets"": 5, ""grenades"": 1, ""shield_time"": 0, ""shield_health"": 0, ""num_deaths"": 0, ""num_shield"": 3}, ""p2"": {""hp"": 60, ""action"": ""grenade"", ""bullets"": 5, ""grenades"": 0, ""shield_time"": 0, ""shield_health"": 0, ""num_deaths"": 0, ""num_shield"": 3}}]";
    
    public Text mqttText;

    // Start is called before the first frame update
    //void Start()
    //{
    //    ProcessReceivedMsg(test_msg);
    //}

    //void Update()
    //{ 
    //    ProcessReceivedMsg(test_msg);
    //}

    // Process the Json message received and update display
    public void ProcessReceivedMsg(string msg)
    {
        UnityEngine.Debug.Log(msg);
        //todo: handle marshal of correct message from requester
        var msgs = Newtonsoft.Json.Linq.JArray.Parse("["+msg+"]");


        foreach (Newtonsoft.Json.Linq.JObject root in msgs)
        {

            //updatePlayer(Newtonsoft.Json.Linq.JObject)
            foreach (KeyValuePair<String, Newtonsoft.Json.Linq.JToken> app in root)
            {
                //updatePlayer()
                //player.doAction()
                var player = app.Key;
                var hp = (String)app.Value["hp"];
                var action = (String)app.Value["action"];
                var bullets = (String)app.Value["bullets"];
                var grenades = (String)app.Value["grenades"];
                var shield_time = (String)app.Value["shield_time"];
                var shield_health = (String)app.Value["shield_health"];
                var num_deaths = (String)app.Value["num_deaths"];
                var num_shield = (String)app.Value["num_shield"];


                mqttText.text = player + hp + action + bullets + grenades + shield_time + shield_health + num_deaths + num_shield;
                UnityEngine.Debug.Log(player + hp + action + bullets + grenades + shield_time + shield_health + num_deaths + num_shield);

                if (player == "p1")
                {
                    //UI
                    ui_manager.Update_PlayerHp(Int32.Parse(hp));
                    ui_manager.Update_PlayerGrenade(Int32.Parse(grenades));
                    ui_manager.Update_PlayerBullet(Int32.Parse(bullets));
                    ui_manager.Update_PlayerShield(Int32.Parse(num_shield));
                    ui_manager.Update_PlayerScore(Int32.Parse(num_deaths));

                    
                    //AR
                    if (string.Equals(action, "shield"))
                    {
                        ar_manager.Player_ShieldAction();
                    }
                    else if (string.Equals(action, "grenade"))
                    {
                        ar_manager.Opponent_GrenadeAction();
                    }
                    ar_manager.Player_ShieldHp(Int32.Parse(shield_health));
                }
                else
                {
                    //UI
                    ui_manager.Update_OpponentHp(Int32.Parse(hp));
                    ui_manager.Update_OpponentGrenade(Int32.Parse(grenades));
                    ui_manager.Update_OpponentBullet(Int32.Parse(bullets));
                    ui_manager.Update_OpponentShield(Int32.Parse(num_shield));
                    ui_manager.Update_OpponentScore(Int32.Parse(num_deaths));


                    //AR
                    if (string.Equals(action, "shield"))
                    {
                        ar_manager.Opponent_ShieldAction();
                    }
                    else if (string.Equals(action, "grenade"))
                    {
                        ar_manager.Player_GrenadeAction();
                    }
                    ar_manager.Opponent_ShieldHp(Int32.Parse(shield_health));
                }



            }
        }
    }

}
