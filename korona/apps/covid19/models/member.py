from django.db import models
from django.utils import timezone


#================================
# 社員情報を管理するモデル
#================================
class Member(models.Model):
    staff_no = models.CharField(
        verbose_name = "社員NO", 
        max_length = 5,
    )
    staff_name = models.CharField(
        verbose_name = "社員名称", 
        max_length = 20,
        blank = True,
        null = True,
    )
    assigned = models.CharField(
        verbose_name = "所属", 
        max_length = 50,
        blank = True,
        null = True,
    )
    email = models.EmailField(
        verbose_name = "メールアドレス", 
        max_length = 254,
        blank = True,
        null = True,
    )
    creator = models.CharField(
        verbose_name = "登録者",
        max_length = 20,
        blank = True,
        null = True,
    )
    created = models.DateTimeField(
        verbose_name = "登録日",
        blank = True,
        null = True,
        auto_now_add = True,        # 登録時に現在時間を設定
    )
    modified = models.DateTimeField(
        verbose_name = "更新日",
        blank = True,
        null = True,
        default = timezone.now,
    )
    
    def __str__(self):
        return self.staff_no + "　:　" + self.staff_name
    
    class Meta:
        app_label = "covid19"
        db_table = "Member"
        verbose_name_plural = "社員マスタ"
