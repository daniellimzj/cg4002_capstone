using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class mqttProcessor : MonoBehaviour
{

    public UI_Manager ui_manager;
    public AR_Manager ar_manager;

    public GameObject invalidActionSign;
    public Text invalidActionText;
    public ParticleSystem bulletEffect;

    public string currPlayer;

    //Audio effects
    public AudioSource sound_shoot;
    public AudioSource sound_reload;
    public AudioSource sound_grenade;
    public AudioSource sound_invalid;


    void Start()
    {
        invalidActionSign.SetActive(false);

        // Set current player (p1 / p2)
        currPlayer = ChangeScene.playerid;
        if (currPlayer == "p1")
        {
            mqttPublisher.topicPublish = "b11/p1_see_p2";
        }
        else
        {
            mqttPublisher.topicPublish = "b11/p2_see_p1";
        }
    }


    public void ProcessReceivedMsg(string msg)
    {
        if (invalidActionSign.activeSelf)
        {
            invalidActionSign.SetActive(false);
        }

        //todo: handle marshal of correct message from requester
        var msgs = Newtonsoft.Json.Linq.JArray.Parse("[" + msg + "]");


        foreach (Newtonsoft.Json.Linq.JObject root in msgs)
        {
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


                UnityEngine.Debug.Log(player + hp + action + bullets + grenades + shield_time + shield_health + num_deaths + num_shield);

                if (player == currPlayer)
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
                        sound_grenade.Play();
                    }
                    else if (string.Equals(action, "logout"))
                    {
                        SceneManager.LoadScene("MenuScene");
                    }
                    else if (string.Equals(action, "shoot"))
                    {
                        UnityEngine.Debug.Log("shoot action");
                        bulletEffect.Play();
                        sound_shoot.Play();
                    }
                    else if (string.Equals(action, "reload"))
                    {
                        sound_reload.Play();
                    }

                    // INVALID ACTIONS
                    else if (string.Equals(action, "grenade_invalid")){
                        //no more grenade
                        invalidActionText.text = "INVALID GRENADE ACTION";
                        invalidActionSign.SetActive(true);
                        sound_invalid.Play();

                    }
                    else if (string.Equals(action, "reload_invalid")){
                        //still have bullet
                        invalidActionText.text = "INVALID RELOAD ACTION";
                        invalidActionSign.SetActive(true);
                        sound_invalid.Play();
                    }
                    else if (string.Equals(action, "shield_invalid")){
                        //no more shield or shield still effective
                        invalidActionText.text = "INVALID SHIELD ACTION";
                        invalidActionSign.SetActive(true);
                        sound_invalid.Play();
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
                    else if (string.Equals(action, "logout"))
                    {
                        SceneManager.LoadScene("MenuScene");
                    }
                    ar_manager.Opponent_ShieldHp(Int32.Parse(shield_health));
                }



            }
        }
    }

}
