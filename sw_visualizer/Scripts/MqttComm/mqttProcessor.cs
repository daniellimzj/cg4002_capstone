using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.UI;

public class mqttProcessor : MonoBehaviour
{

    //string test_msg = @"[{""p1"": {""hp"": 30, ""action"": ""grenade"", ""bullets"": 5, ""grenades"": 1, ""shield_time"": 0, ""shield_health"": 0, ""num_deaths"": 0, ""num_shield"": 3}, ""p2"": {""hp"": 60, ""action"": ""grenade"", ""bullets"": 5, ""grenades"": 0, ""shield_time"": 0, ""shield_health"": 0, ""num_deaths"": 0, ""num_shield"": 3}}]";
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
        var getMsgs = Newtonsoft.Json.Linq.JArray.Parse(msg);

        foreach (Newtonsoft.Json.Linq.JObject root in getMsgs)
        {
            foreach (KeyValuePair<String, Newtonsoft.Json.Linq.JToken> app in root)
            {
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
            }
        }
    }

}
