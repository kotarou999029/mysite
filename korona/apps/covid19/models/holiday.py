from django.db import models
from django.utils import timezone


#================================
# 社員休日情報を管理するモデル
#================================
class Holiday(models.Model):
    staff_no = models.CharField(
        verbose_name = "社員NO", 
        max_length = 5,
    )
    h_date = models.DateField(
        verbose_name = "日付",
        blank = True,
        null = True,
    )
    flag_choices = (
        ("",""),
        (1,  "公休日"),
        (2,  "有給休暇"),
        (3,  "午前半休"),
        (4,  "午後半休"),
        (5,  "代替休日"),
        (6,  "振替休日"),
        (7,  "会社都合"),
        (8,  "夏季休暇"),
        (9,  "慶弔休暇"),
        (10, "病気休暇"),
        (11, "リフレッシュ休暇"),
        (99, "その他"),
    )
    flag = models.IntegerField(
        verbose_name = "フラグ",
        blank = True,
        null = True,
        choices = flag_choices,
    )
    note = models.TextField(
        verbose_name = "内容",
        max_length = 1000,
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
        return self.staff_no + "　:　" + str(self.h_date)
    
    class Meta:
        app_label = "covid19"
        db_table = "Holiday"
        verbose_name_plural = "社員休日マスタ"
