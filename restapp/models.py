from django.db import models

class Customer(models.Model):
     name = models.CharField(max_length=256,verbose_name = '이름')
     phone = models.CharField(primary_key=True,max_length=256, verbose_name = '전화번호')
     password = models.CharField(max_length=256, verbose_name = '비밀번호')
     
     def __str__(self):
          return self.phone

     class Meta():
          db_table = '예약자 명단'
          verbose_name = '예약자 명단'
          verbose_name_plural = '예약자 명단'

class ReservTime(models.Model):
     time = models.CharField(max_length =256 , verbose_name = '예약시간')
     def __str__(self):
          return self.time
     
     class Meta():
          db_table = '예약시간'
          verbose_name = '예약시간'
          verbose_name_plural = '예약시간'

class Tables(models.Model):
     table = models.CharField(max_length =256 , verbose_name="테이블번호")
     def __str__(self):
          return self.table
     class Meta():
          db_table = '테이블'
          verbose_name = '테이블'
          verbose_name_plural = '테이블'

class ReservState(models.Model):
     reserv = models.CharField(max_length=256,verbose_name='예약상태')

     def __str__(self):
          return self.reserv
     class Meta():
          db_table = '예약state'
          verbose_name ='예약 상태'
          verbose_name_plural = '예약상태'

class Reservation(models.Model):
     table = models.ForeignKey('restapp.Tables', on_delete=models.CASCADE, verbose_name = '테이블')
     party = models.ForeignKey('restapp.Customer', on_delete=models.CASCADE, verbose_name = '예약자')
     spot = models.DateField(verbose_name='날짜')
     time = models.ForeignKey('restapp.ReservTime',on_delete=models.CASCADE, verbose_name = '예약시간')
     party_num = models.IntegerField(verbose_name = '예약자일행')
     Reserv_day = models.DateTimeField(auto_now_add=True)
     reserv = models.ForeignKey('restapp.ReservState',on_delete=models.CASCADE,verbose_name = '상태')

     class Meta():
          db_table = '예약 명단'
          verbose_name = '예약 명단'
          verbose_name_plural = '예약 명단'