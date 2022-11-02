using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Numerics;
using UnityEngine;

public class GrenadeThrow : MonoBehaviour
{

    public float throwForce = 30f;
    float countDown;
    float delay = 2f;
    bool grenadeFlying = false;

    public GameObject grenadePrefab;
    public Transform grenadeTransform;
    GameObject grenade;

    public void ThrowGrenade(int direction)
    {
        if (direction == 0) //fly to opponent
        {
            UnityEngine.Debug.Log("grenade throw 0");
            countDown = delay;
            grenadeFlying = true;

            grenade = Instantiate(grenadePrefab, transform.position, transform.rotation);
            Rigidbody rb = grenade.GetComponent<Rigidbody>();
            rb.AddForce(transform.forward * throwForce, ForceMode.VelocityChange);
        }
        else if (direction == 1) //fly to player
        {
            UnityEngine.Debug.Log("grenade throw 1");
            countDown = delay;
            grenadeFlying = true;

            grenade = Instantiate(grenadePrefab, transform.position + transform.forward * grenadeTransform.position.z, transform.rotation);
            UnityEngine.Debug.Log(grenade.transform.position);

            Rigidbody rb = grenade.GetComponent<Rigidbody>();
            rb.AddForce(transform.forward * -1 * 20f, ForceMode.VelocityChange);
        }
        
    }

    void Update()
    {
        countDown -= Time.deltaTime;
        if (countDown <= 0f && grenadeFlying)
        {
            Destroy(grenade);
            grenadeFlying = false;
        }
    }


}
