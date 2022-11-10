using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AR_Manager : MonoBehaviour
{
    public AREffect playerAR;
    public AREffect opponentAR;


    // worker functions
    public void Player_ShieldAction()
    {
        playerAR.showShieldAR();

    }

    public void Player_ShieldHp(int hp)
    {
        playerAR.SetShieldHpAR(hp);
    }

    public void Opponent_ShieldAction()
    {
        opponentAR.showShieldAR();
    }

    public void Opponent_ShieldHp(int hp)
    {
        opponentAR.SetShieldHpAR(hp);
    }



    public void Player_GrenadeAction()
    {
        playerAR.showPlayerGrenadeAR(1);
    }

    public void Opponent_GrenadeAction()
    {
        opponentAR.showPlayerGrenadeAR(0);
    }

}
