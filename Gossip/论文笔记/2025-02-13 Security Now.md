# SECURITY NOW!

> 记录一部分看过的 Security Now! 播客中谈到身份认证方面或者其它感兴趣的内容，可能会增加一些自己的思考

## Episode # 1011 

### Bitwarden 改善账户安全性

为了增强账户安全性并保护那些没有启用双因素认证的用户账户，Bitwarden要求尝试在从未使用过的设备上登录时，需要进行电子邮件验证才能完成最终的账户登录。这样的措施可以防止当攻击者获得Bitwarden凭证时，可以直接登录 Bitwarden 并且获取存储在其中的所有数据。如果没有启用双因素认证，则必须采用邮件认证。

尽管如此，启用双因素认证一定是更加安全的，因为电子邮件作为认证的方法的安全性是不足的。

**个人思考：** 口令管理器在为账户安全提供更多的保障，例如仅使用传统凭证不能登录成功，其中采用的方法包括 Risk-based Authentication 判断登录环境是否安全，以及要求启用双因素认证等。

## Episode # 1008

### 对于 Time-Varying Six-Digit One-time tokens 的研究

**Apophenia:** the tendency to perceive a connection or meaningful pattern between unrelated or random things (such as objects or ideas). 在这篇播客中，作者提到是 `tendency to see patterns in random noise where none exist.` 即看上去有规律的数据是否仍然是随机的。

有用户反馈发现认证器产生的六位代码总是包括一个或者多个重复的数字，根据计算，大约15%的六位数字包含六个独立的数字，感觉重复的数字比应有的多。但是发现，代码中只有三到四个独特的数字，例如906090 或者 131327，倾向于一种重复的模式。因为30s就会刷新一次，暴力破解二次身份认证代码是相对困难的。但是为什么这些Authenticator倾向于产生一些简化的代码呢？

存在特定的RFC定义OTP的标准

Time-Based One-Time Password 👉 RFC 6238 2011
HMAC-Based One-Time Password 👉 RFC 4226 2005

此处可以发现，虽然作者发现了一定的规律，但是奈何带有重复数字的内容过于多

Whether the 80-bit keys that most sites give authenticators to use are long enough to contain sufficient entroy. 大多数网站给定的80bit长度的密钥是否足够长，具有足够的熵值

> 此处给定的 80 bit 是否正确还有待考量。

广泛使用的二维码用于设置 TOTP，没有在任何 RFC 中定义，而是由 Google Authenticator 首次提出，将密钥编码为Base32字符串。

### 邮件安全

作者提到认为邮件是非常不安全的，并且提到这是 PIN 和 口令的恢复方法

**问题：** 

1. 生成的OTP真的是随机的吗？
2. 

## Episode # 980
