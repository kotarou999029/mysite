from django.db import models
from django.utils import timezone


#================================
# 体調を管理するモデル
#================================
class Health(models.Model):
    staff_no = models.CharField(
        verbose_name = "社員NO", 
        max_length = 5,
    )
    reported = models.DateField(
        verbose_name = "報告日",
    )
    # 00.0 度
    degrees = models.DecimalField(
        verbose_name = "体温",
        max_digits = 3,
        decimal_places = 1,
        blank = True,
        null = True,
    )
    condition_choices = (
        ("",""),
        (True,  "異常なし"),
        (False, "異常あり"),
    )
    condition = models.BooleanField(
        verbose_name = "体調",
        blank = True,
        null = True,
        default = "",
        choices = condition_choices,
    )
    note = models.TextField(
        verbose_name = "備考",
        max_length = 1000,
        blank = True,
        null = True,
    )
    is_deleted = models.BooleanField(
        verbose_name = "削除フラグ",
        default = False,
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
        return ( self.staff_no + "　:　"
            + str(self.reported) + "　:　"
            + str(self.degrees)  + " 度"
        )
    
    class Meta:
        app_label = "covid19"
        db_table = "Health"
        verbose_name_plural = "体調管理DB"
