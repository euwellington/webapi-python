class script:
    def getAll():
        script =    """
                         SELECT 
                            e.id as id,
                            eq.nome as equipamento,
                            u.nome as usuarioNome,
                            a.nome as acionamentoNome,
                            e.dataHora as dataHoraEvento
                        FROM
                            eventos AS e
                        INNER JOIN
                            usuarios AS u
                        ON 
                            u.id = e.usuarioId 
                        INNER JOIN
                            equipamentos AS eq
                        ON 
                            eq.id = e.equipamentoId 
                        INNER JOIN
                            acionamentos AS a
                        ON 
                            a.id = e.acionamentoId 
                        AND
                            a.equipamentoId = e.equipamentoId
                    """
        return script