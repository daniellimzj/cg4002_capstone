using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{

    // Health
    public HealthBar healthBar;
    public int maxHealth = 100;
    public int currentHealth;

    // Shield
    public Shield shield;
    public int maxShield = 2;
    public int currentShield;

    // Grenade
    public Grenade grenade;
    public int maxGrenade = 3;
    public int currentGrenade;

    // Bullet
    public Bullet bullet;
    public int maxBullet = 6;
    public int currentBullet;
    

    // Start is called before the first frame update
    void Start()
    {

        currentHealth = maxHealth;
        healthBar.SetMaxHealth(maxHealth);

        currentShield = maxShield;
        shield.SetShieldCount(maxShield);

        currentGrenade = maxGrenade;
        grenade.SetGrenadeCount(maxGrenade);

        currentBullet = maxBullet;
        bullet.SetBulletCount(maxBullet);

    }


    public void SetHealth(int hp)
    {
        healthBar.SetHealth(hp);
    }

    public void SetShield(int num)
    {
        shield.SetShieldCount(num);
    }

    public void SetGrenade(int num)
    {
        grenade.SetGrenadeCount(num);
    }

    public void SetBullet(int num)
    {
        bullet.SetBulletCount(num);
    }
}

//func create