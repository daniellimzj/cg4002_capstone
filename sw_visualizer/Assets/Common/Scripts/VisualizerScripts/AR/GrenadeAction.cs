using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class GrenadeAction : MonoBehaviour
{

    public float delay = 2f;
    

    public GameObject explosionGO;
    public GrenadeThrow grenadeThrow;

    float countDown;
    bool hasExploded = true;
    bool explosionPlaying = false;

    // Start is called before the first frame update
    public void StartGrenade(int direction)
    {
        countDown = delay;
        hasExploded = false;
        grenadeThrow.ThrowGrenade(direction);
    }


    void Update()
    {
        countDown -= Time.deltaTime;
        if (countDown <= 0f && !hasExploded)
        {
            Explode();
            explosionPlaying = true;
            hasExploded = true;
        }
        if (countDown <= -3f && explosionPlaying)
        {
            explosionGO.SetActive(false);
            explosionPlaying = false;
        }
    }

    

    void Explode()
    {
        if (!explosionGO.activeSelf)
        {
            explosionGO.SetActive(true);
        }
    }
}
