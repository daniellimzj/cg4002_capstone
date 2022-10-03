using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AR_Manager : MonoBehaviour
{
    public AREffect playerAR;
    public AREffect opponentAR;

    public GameObject markerSignal;

    void start()
    {
        markerSignal.SetActive(false);
    }

    // worker functions
    public void Player_ShieldAction()
    {
        playerAR.showShieldAR();

    }

    public void Opponent_ShieldAction()
    {
        opponentAR.showShieldAR();
    }

    public void Player_GrenadeAction()
    {
        playerAR.showPlayerGrenadeAR(1);
    }

    public void Opponent_GrenadeAction()
    {
        opponentAR.showPlayerGrenadeAR(0);
    }




    // AR marker
    public void MarkerFound()
    {
        markerSignal.SetActive(true);
    }

    public void MarkerLost()
    {
        markerSignal.SetActive(false);
    }
}
