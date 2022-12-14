using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TestButton : MonoBehaviour
{

    public Player player;
    public AREffect arEffect;
    public Score score;

    public void Test_TakeDamageButton()
    {
        player.SetHealth(10);
    }

    public void Test_UseShield()
    {
        player.SetShield(100);
    }

    public void Test_UseGrenade()
    {
        player.SetGrenade(100);
    }

    public void Test_UseBullet()
    {
        player.SetBullet(100);
    }

    public void Test_ShowShield()
    {
        arEffect.showShieldAR();
    }

    public void Test_RemoveShield()
    {
        arEffect.SetShieldHpAR(10);

    }

    public void Test_ShowGrenade()
    {
        arEffect.showPlayerGrenadeAR(0); //fly to opponent
    }

    public void Test_ShowGrenade2()
    {
        arEffect.showPlayerGrenadeAR(1); //fly to player
    }

    public void Test_RemoveGrenade()
    {
        arEffect.removeGrenadeAR();
    }

    public void AddPlayerScore()
    {
        score.ChangePlayerScore();
    }

    public void AddOpponentScore()
    {
        score.ChangeOpponentScore();
    }
}
