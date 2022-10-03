using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class UI_Manager : MonoBehaviour
{
    public Player player;
    public Player opponent;
    public Score score;



    // worker functions
    // player
    public void Update_PlayerHp(int hp)
    {
        player.SetHealth(hp);
    }

    public void Update_PlayerGrenade(int num)
    {
        player.SetGrenade(num);
    }

    public void Update_PlayerBullet(int num)
    {
        player.SetBullet(num);
    }

    public void Update_PlayerShield(int num)
    {
        player.SetShield(num);
    }

    //opponent
    public void Update_OpponentHp(int hp)
    {
        opponent.SetHealth(hp);
    }

    public void Update_OpponentGrenade(int num)
    {
        opponent.SetGrenade(num);
    }

    public void Update_OpponentBullet(int num)
    {
        opponent.SetBullet(num);
    }

    public void Update_OpponentShield(int num)
    {
        opponent.SetShield(num);
    }


    //score
    public void Update_Score(int d1, int d2)
    {
        score.UpdateScore(d1, d2);
    }
    public void Update_PlayerScore(int d)
    {
        score.UpdatePlayerScore(d);
    }
    public void Update_OpponentScore(int d)
    {
        score.UpdateOpponentScore(d);
    }
}

