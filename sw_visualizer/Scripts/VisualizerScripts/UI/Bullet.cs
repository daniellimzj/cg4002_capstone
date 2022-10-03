using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Bullet : MonoBehaviour
{
    public Text bulletText;

    public void SetBulletCount(int bulletCount)
    {
        bulletText.text = bulletCount.ToString();
    }
}
