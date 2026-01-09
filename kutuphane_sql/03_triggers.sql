Create OR Replace Function fn_log_kayit()
Returns Trigger
Language plpgsql
AS $$
Begin
	Insert Into log_kayitlari(
		tablo_adi,
		islem_turu,
		islem_yapan_kullanici_id,
		aciklama
	)
	Values(
		TG_TABLE_NAME,
		INITCAP(Lower(Tg_OP)),
		current_setting('application.user_id', true)::INT,
		'Otomatik Log Kaydı'
	);

	Return Coalesce(New, Old);
End;
$$;

Create Trigger trg_log_odunc
After Insert OR Update OR Delete
on odunc
For Each Row
Execute Function fn_log_kayit();

Create Trigger trg_log_kitaplar
After Update
on kitaplar
For Each Row
Execute Function fn_log_kayit();

Create Trigger trg_log_cezalar
After Insert
on cezalar
For Each Row
Execute Function fn_log_kayit();
