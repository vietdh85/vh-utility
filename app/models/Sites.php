<?php

class Sites extends ModelBase
{
    public $id;
    public $url;
    public $name;
    public $start_at;	
	public $end_at;
	public $type;
	public $is_scam;

    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'sites';
    }

    /**
     * Allows to query a set of records that match the specified conditions
     *
     * @param mixed $parameters
     * @return Words[]
     */
    public static function find($parameters = null)
    {
        return parent::find($parameters);
    }

    /**
     * Allows to query the first record that match the specified conditions
     *
     * @param mixed $parameters
     * @return Words
     */
    public static function findFirst($parameters = null)
    {
        return parent::findFirst($parameters);
    }

	public static function getList(){
        $phql = "SELECT s.*
			FROM Sites s
			WHERE s.is_scam = 0
			ORDER BY s.start_at desc, s.id ASC";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
	
}
