using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AREffect : MonoBehaviour
{

    public GameObject shieldGO, shieldActionGO, timerGO, explosionGO, grenadeActionGO;
    public ShieldAction shieldAction;
    public GrenadeAction grenadeAction;
    public CountDownTimer countDownTimer;

    public int maxHp = 30;
    public int currentHp;



    // Start is called before the first frame update
    void Start()
    {
        //shield
        currentHp = maxHp;
        shieldGO.SetActive(false);
        shieldActionGO.SetActive(false);
        timerGO.SetActive(false);

        //grenade
        explosionGO.SetActive(false);
        //grenadeGO.SetActive(false);

    }

    // Shield
    public void showShieldAR()
    {
        activateShieldAR();
        currentHp = maxHp;
        shieldAction.SetShieldActionText(currentHp);
        countDownTimer.startTimer();
        
    }

    public void SetShieldHpAR(int hp)
    {
        currentHp = hp;
        shieldAction.SetShieldActionText(currentHp);

        if (currentHp <= 0)
        {
            deactivateShieldAR();
        }
    }

    public void activateShieldAR()
    {
        timerGO.SetActive(true);
        shieldGO.SetActive(true);
        shieldActionGO.SetActive(true);
    }

    public void deactivateShieldAR()
    {
        shieldGO.SetActive(false);
        shieldActionGO.SetActive(false);
        timerGO.SetActive(false);
    }



    // Grenade
    public void showPlayerGrenadeAR(int direction)
    {
        grenadeAction.StartGrenade(direction);
    }

    public void removeGrenadeAR()
    {
        explosionGO.SetActive(false);
    }
}
